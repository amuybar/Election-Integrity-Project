from django.shortcuts import render, redirect
from django.contrib import messages
from .models import IncidentReport 
from .forms import IncidentReportForm


def report_incident(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save()
            messages.success(request, 'Your incident report has been submitted successfully.')
            return redirect('report_confirmation', incident_id=incident.id)
    else:
        form = IncidentReportForm()
    
    return render(request, 'reporting/report_incident.html', {'form': form})

def report_confirmation(request, incident_id):
    incident = IncidentReport.objects.get(id=incident_id)
    return render(request, 'reporting/report_confirmation.html', {'incident': incident})


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
