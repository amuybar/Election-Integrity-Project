from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import IncidentReport 
from .forms import IncidentReportForm

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

# Election Dashboard
def dashboard_view(request):
    return render(request, 'reporting/dashboard.html')

# Voter Education
def voter_education_view(request):
    return render(request, 'reporting/voter_education.html')

# Notifications
def notifications_view(request):
    return render(request, 'reporting/notifications.html')

# Language Selection
def language_view(request):
    return render(request, 'reporting/language.html')