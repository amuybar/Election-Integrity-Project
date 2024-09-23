from django.db import models
from django.contrib.auth import get_user_model

class Incident(models.Model):
    INCIDENT_TYPES = (
        ('fraud', 'Fraud'),
        ('tampering', 'Ballot Tampering'),
        ('intimidation', 'Voter Intimidation'),
    )
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPES)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    reported_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.incident_type} reported by {self.reported_by}"
