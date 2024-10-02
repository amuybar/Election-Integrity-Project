# user/urls.py

from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('password_reset/', views.password_reset, name='password_reset'),

]
