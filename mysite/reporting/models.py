# REPORT INCIDENT MODEL
from django.db import models
from django.utils import timezone

class IncidentReport(models.Model):
    INCIDENT_TYPES = [
        ('voter_intimidation', 'Voter Intimidation'),
        ('machine_malfunction', 'Voting Machine Malfunction'),
        ('long_wait_times', 'Long Wait Times'),
        ('misinformation', 'Misinformation'),
        ('other', 'Other'),
    ]

    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPES)
    location = models.CharField(max_length=255)
    date_time = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    evidence = models.FileField(upload_to='incident_evidence/', blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"{self.get_incident_type_display()} at {self.location}"