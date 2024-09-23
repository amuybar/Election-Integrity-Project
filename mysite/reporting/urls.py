from django.urls import path
from . import views

app_name = 'reporting'

urlpatterns = [
    path('incident/', views.report_incident, name='report_incident'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
