from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['incident_type', 'location', 'description', 'image']
