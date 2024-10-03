from django.urls import path
from . import views

app_name = 'reporting'

urlpatterns = [
    # Report Incident
    path('incident/', views.report_incident, name='report_incident'),
    path('report_confirmation/<int:incident_id>/', views.report_confirmation, name='report_confirmation'),

    # Incident Map
    path('incident_map/', views.incident_map_view, name='incident_map'),

    # Election Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard_view'),

    # Voter Education
    path('voter_education/', views.voter_education_view, name='voter_education'),

    # Notifications
    path('notifications/', views.notifications_view, name='notifications'),

    # Language Selection
    path('language/', views.language_view, name='language'),
]