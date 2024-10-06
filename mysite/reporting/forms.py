from django import forms
from .models import IncidentReport, ElectionResult

# Form for IncidentReport Model


class IncidentReportForm(forms.ModelForm):
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
    ALLOWED_FILE_TYPES = ['image/jpeg', 'image/png']

    class Meta:
        model = IncidentReport
        fields = [
            'incident_type',
            'location',
            'date_time',
            'description',
            'evidence',
            'contact_info',
            'county',
            'constituency',
            'polling_station',
            'latitude',
            'longitude',
        ]

        widgets = {
            'incident_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'evidence': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'}),
            'county': forms.Select(attrs={'class': 'form-control'}),
            'constituency': forms.Select(attrs={'class': 'form-control'}),
            'polling_station': forms.Select(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # Custom validation for the evidence field
    def clean_evidence(self):
        evidence = self.cleaned_data.get('evidence')

        if evidence:
            # Validate file size
            if evidence.size > self.MAX_FILE_SIZE:
                raise forms.ValidationError(f"File size exceeds {self.MAX_FILE_SIZE / (1024 * 1024)} MB limit.")

            # Validate file type
            if evidence.content_type not in self.ALLOWED_FILE_TYPES:
                raise forms.ValidationError("Only JPEG and PNG image files are allowed.")

        return evidence

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
