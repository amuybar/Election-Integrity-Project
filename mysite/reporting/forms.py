# REPORT INCIDENT FORM
from django import forms
from .models import IncidentReport

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ['incident_type', 'location', 'date_time', 'description', 'evidence', 'contact_info']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_evidence(self):
        evidence = self.cleaned_data.get('evidence')
        if evidence:
            file_size = evidence.size
            max_size = 10 * 1024 * 1024  # 10 MB
            if file_size > max_size:
                raise forms.ValidationError("File size must be no more than 10 MB.")
            file_type = evidence.content_type.split('/')[0]
            if file_type not in ['image', 'video']:
                raise forms.ValidationError("Only image or video files are allowed.")
        return evidence