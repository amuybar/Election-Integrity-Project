from django.contrib import admin
from .models import IncidentReport, ElectionResult,County, Constituency, PollingStation

# Register your models here
@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ('incident_type',
            'location',
            'date_time',
            'description',
            'evidence',
            'contact_info',
            'county',
            'constituency',
            'polling_station',
            'latitude',
            'longitude',)  
    search_fields = ('incident_type', 'location', 'county')  
    list_filter = ('county', 'constituency', 'polling_station')  

@admin.register(ElectionResult)
class ElectionResultAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'votes', 'county', 'polling_station')
    search_fields = ('candidate', 'county')
    list_filter = ('county', 'constituency', 'polling_station')





@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Constituency)
class ConstituencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'county')
    list_filter = ('county',)

@admin.register(PollingStation)
class PollingStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'constituency')
    list_filter = ('constituency',)
