from django.db import models
from django.contrib.auth.models import AbstractUser

# Define your roles here
ROLES = [
    ('citizen', 'Citizen'),
    ('monitor', 'Monitor'),
    ('official', 'Official'),
]

class CustomUser(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLES, default='citizen')
    
    # Avoid clash with Django's auth.User model for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change to avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Change to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
