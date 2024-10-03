from django import forms
from .models import IncidentReport, ElectionResult

# Form for IncidentReport Model
class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ['incident_type', 'location', 'date_time', 'description', 'evidence', 'contact_info']

        # Customize widget styles if needed
        widgets = {
            'incident_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'evidence': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Form for ElectionResult Model
class ElectionResultForm(forms.ModelForm):
    class Meta:
        model = ElectionResult
        fields = ['candidate', 'votes', 'county', 'constituency', 'polling_station']

        # Customize widget styles if needed
        widgets = {
            'candidate': forms.TextInput(attrs={'class': 'form-control'}),
            'votes': forms.NumberInput(attrs={'class': 'form-control'}),
            'county': forms.Select(attrs={'class': 'form-control'}),
            'constituency': forms.Select(attrs={'class': 'form-control'}),
            'polling_station': forms.Select(attrs={'class': 'form-control'}),
        }
