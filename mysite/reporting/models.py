from django.db import models
from django.utils import timezone


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='candidates/')  # Image field for candidate pictures

    def __str__(self):
        return self.name



class County(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Constituency(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PollingStation(models.Model):
    name = models.CharField(max_length=100)
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    registered_voters = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ElectionResult(models.Model):
    POSITION_CHOICES = [
        ('president', 'President'),
        ('governor', 'Governor'),
        ('senator', 'Senator'),
        ('mp', 'Member of Parliament'),
        ('mca', 'Member of County Assembly'),
    ]

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)  # Change from CharField to ForeignKey
    votes = models.IntegerField()
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    polling_station = models.ForeignKey(PollingStation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidate.name} - {self.get_position_display()} - {self.votes} votes"


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
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE, null=True, blank=True)
    polling_station = models.ForeignKey(PollingStation, on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_incident_type_display()} at {self.location}"