from django.shortcuts import render

# Report Incident
def report_incident_view(request):
    return render(request, 'reporting/report_incident.html')

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
