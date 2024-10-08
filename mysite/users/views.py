from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import get_backends
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm  
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages

# LOGIN VIEW
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Set the session expiry if 'remember_me' is checked
                if request.POST.get('remember_me'):
                    # Session lasts for 30 days
                    request.session.set_expiry(timedelta(days=30))  
                return redirect('home')  
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})
# LOGOUT  VIEW
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

# PRIFILE VIEW
def profile_view(request):
    return render(request, 'users/profile.html')

# SIGNUP VIEW
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Specify the backend manually
            backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user, backend=backend)  # Log the user in after successful signup
            return redirect('home')  # Redirect to home after signup
        else:
            messages.error(request, "Please correct the errors below.")  # Show errors if form is invalid
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/signup.html', {'form': form})

# RESET PASSWORD VIEW
def password_reset(request):
    return render(request, 'users/password_reset.html')
