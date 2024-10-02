
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('features/', views.features, name='features'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('contact/', views.contact, name='contact'),


]
 