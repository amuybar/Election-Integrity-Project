from django.shortcuts import render
from .forms import IncidentForm

def report_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = IncidentForm()
    return render(request, 'reporting/report.html', {'form': form})

def dashboard_view(request):
    return render(request, 'reporting/dashboard.html')
