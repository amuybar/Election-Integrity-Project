from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import IncidentReport 
from .forms import IncidentReportForm


from django.http import JsonResponse
from .models import ElectionResult, IncidentReport, County, Constituency, PollingStation

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
    # Fetch the incident report object
    incident = get_object_or_404(IncidentReport, id=incident_id)
    
    # You can extract more details to pass to the template if necessary
    reference_number = incident.date_time 
    confirmation_message = "Thank you for reporting the incident. Your report has been submitted successfully."

    # Render the confirmation page with more context
    return render(request, 'reporting/report_confirmation.html', {
        'incident': incident,
        'reference_number': reference_number,  
        'confirmation_message': confirmation_message  
    })

# Incident Map
def incident_map_view(request):
    return render(request, 'reporting/incident_map.html')


# Election Dashboard View
def dashboard_view(request):
    # Fetch filter options from the database (Counties, Constituencies, etc.)
    counties = County.objects.all()
    constituencies = Constituency.objects.all()
    polling_stations = PollingStation.objects.all()

    # Default: Load results without filters (could also set defaults to show recent results)
    results = ElectionResult.objects.all()
    
    # Filter by County if selected
    selected_county = request.GET.get('county')
    if selected_county:
        results = results.filter(county__name=selected_county)

    # Filter by Constituency if selected
    selected_constituency = request.GET.get('constituency')
    if selected_constituency:
        results = results.filter(constituency__name=selected_constituency)

    # Filter by Polling Station if selected
    selected_polling_station = request.GET.get('polling_station')
    if selected_polling_station:
        results = results.filter(polling_station__name=selected_polling_station)

    # Fetch incidents and pass them for visualization on the map
    incidents = IncidentReport.objects.all()

    context = {
        'counties': counties,
        'constituencies': constituencies,
        'polling_stations': polling_stations,
        'results': results,
        'incidents': incidents,
    }

    return render(request, 'reporting/dashboard.html', context)

# JSON API to handle dynamic filtering via AJAX (optional)
def filter_results(request):
    county = request.GET.get('county', None)
    constituency = request.GET.get('constituency', None)
    polling_station = request.GET.get('polling_station', None)

    results = ElectionResult.objects.all()

    if county:
        results = results.filter(county__name=county)
    if constituency:
        results = results.filter(constituency__name=constituency)
    if polling_station:
        results = results.filter(polling_station__name=polling_station)

    # Prepare data for JSON response
    data = {
        'results': list(results.values('candidate', 'votes', 'polling_station__name', 'constituency__name', 'county__name'))
    }

    return JsonResponse(data)


# Voter Education
def voter_education_view(request):
    return render(request, 'reporting/voter_education.html')

# Notifications
def notifications_view(request):
    return render(request, 'reporting/notifications.html')

# Language Selection
def language_view(request):
    return render(request, 'reporting/language.html')