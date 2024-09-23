from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # INCLUDING APPS
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  
    path('reporting/', include('reporting.urls')),  
    path('', include('home.urls')),  
]
