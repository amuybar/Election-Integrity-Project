from django.urls import path
from . import views

app_name = 'reporting'

urlpatterns = [
    # Report Incident
    path('incident/', views.report_incident_view, name='report_incident'),

    # Incident Map
    path('incident_map/', views.incident_map_view, name='incident_map'),

    # Election Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Voter Education
    path('voter_education/', views.voter_education_view, name='voter_education'),

    # Notifications
    path('notifications/', views.notifications_view, name='notifications'),

    # Language Selection
    path('language/', views.language_view, name='language'),
]
