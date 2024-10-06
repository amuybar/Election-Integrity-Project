from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, F
from django.http import JsonResponse
from .models import ElectionResult, IncidentReport, County, Constituency, PollingStation
from .forms import IncidentReportForm

def dashboard_view(request):
    # Fetch filter options from the database
    counties = County.objects.all()
    constituencies = Constituency.objects.none()
    polling_stations = PollingStation.objects.none()

    # Initialize the queryset for election results
    results = ElectionResult.objects.all()

    # Apply filters based on user input
    county_id = request.GET.get('county')
    constituency_id = request.GET.get('constituency')
    polling_station_id = request.GET.get('polling_station')
    search_query = request.GET.get('search')

    if county_id:
        results = results.filter(county_id=county_id)
        constituencies = Constituency.objects.filter(county_id=county_id)
        if constituency_id:
            results = results.filter(constituency_id=constituency_id)
            polling_stations = PollingStation.objects.filter(constituency_id=constituency_id)
            if polling_station_id:
                results = results.filter(polling_station_id=polling_station_id)

    if search_query:
        results = results.filter(candidate__name__icontains=search_query)  # Updated to filter candidate name correctly

    # Get presidential results
    presidential_results = results.filter(position='president').values('candidate__name', 'candidate__image').annotate(
        total_votes=Sum('votes'),
        percentage=Sum('votes') * 100.0 / Sum('votes', filter=F('position')=='president')
    ).order_by('-total_votes')

    # Calculate turnout percentage
    total_registered_voters = PollingStation.objects.aggregate(total=Sum('registered_voters'))['total'] or 1
    total_votes = results.aggregate(total=Sum('votes'))['total'] or 0
    turnout_percentage = (total_votes / total_registered_voters) * 100

    # Prepare polling station data
    polling_stations = PollingStation.objects.annotate(
        total_votes=Sum('electionresult__votes'),
        turnout_percentage=F('total_votes') * 100.0 / F('registered_voters')
    ).filter(id=polling_station_id) if polling_station_id else PollingStation.objects.annotate(
        total_votes=Sum('electionresult__votes'),
        turnout_percentage=F('total_votes') * 100.0 / F('registered_voters')
    )

    # Fetch incident reports
    incidents = IncidentReport.objects.all()

    context = {
        'counties': counties,
        'constituencies': constituencies,
        'polling_stations': polling_stations,
        'results': results,
        'presidential_results': presidential_results,
        'incidents': incidents,
        'turnout_percentage': turnout_percentage,
    }

    return render(request, 'reporting/dashboard.html', context)

def filter_results(request):
    county_id = request.GET.get('county')
    constituency_id = request.GET.get('constituency')
    polling_station_id = request.GET.get('polling_station')

    constituencies = Constituency.objects.filter(county_id=county_id) if county_id else Constituency.objects.none()
    polling_stations = PollingStation.objects.filter(constituency_id=constituency_id) if constituency_id else PollingStation.objects.none()

    results = ElectionResult.objects.all()

    if county_id:
        results = results.filter(county_id=county_id)

    if constituency_id:
        results = results.filter(constituency_id=constituency_id)

    if polling_station_id:
        results = results.filter(polling_station_id=polling_station_id)

    data = {
        'results': list(results.values('candidate', 'votes', 'position', 'polling_station__name', 'constituency__name', 'county__name')),
        'constituencies': list(constituencies.values('id', 'name')),
        'polling_stations': list(polling_stations.values('id', 'name')),
    }

    return JsonResponse(data)

def report_incident(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save()
            messages.success(request, 'Your incident report has been submitted successfully.')
            return redirect('reporting:report_confirmation', incident_id=incident.id)
    else:
        form = IncidentReportForm()
    
    return render(request, 'reporting/report_incident.html', {'form': form})

def report_confirmation(request, incident_id):
    incident = get_object_or_404(IncidentReport, id=incident_id)
    reference_number = f"INC-{incident.id:05d}"
    confirmation_message = "Thank you for reporting the incident. Your report has been submitted successfully."

    return render(request, 'reporting/report_confirmation.html', {
        'incident': incident,
        'reference_number': reference_number,
        'confirmation_message': confirmation_message
    })


# INCIDENT MAP VIEW
def incident_map_view(request):
    # Fetch all incident reports from the database
    incidents = IncidentReport.objects.all()
    
    # Prepare data to send to the template
    incident_data = [
        {
            'id': incident.id,
            'latitude': incident.latitude,  # Assuming you have a latitude field
            'longitude': incident.longitude,  # Assuming you have a longitude field
            'description': incident.description,  # Assuming you have a description field
        }
        for incident in incidents
    ]

    return render(request, 'reporting/incident_map.html', {'incidents': incident_data})

def voter_education_view(request):
    # Placeholder for voter education content
    return render(request, 'reporting/voter_education.html')

def notifications_view(request):
    # Placeholder for notifications fetching logic
    notifications = []  # Replace with actual notification fetching logic
    return render(request, 'reporting/notifications.html', {'notifications': notifications})

def language_view(request):
    # Placeholder for language selection logic
    available_languages = ['en', 'sw', 'fr']  # Example languages
    return render(request, 'reporting/language.html', {'available_languages': available_languages})

def election_results_api(request):
    # API endpoint for fetching election results
    results = ElectionResult.objects.all()
    data = list(results.values('candidate', 'votes', 'position', 'polling_station__name', 'constituency__name', 'county__name'))
    return JsonResponse({'results': data})

def incident_report_api(request):
    # API endpoint for submitting incident reports
    if request.method == 'POST':
        form = IncidentReportForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save()
            return JsonResponse({'status': 'success', 'incident_id': incident.id})
        return JsonResponse({'status': 'error', 'errors': form.errors})

    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})
