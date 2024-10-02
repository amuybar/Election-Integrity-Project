from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm  # Ensure this is imported
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages

# Login View
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
                    request.session.set_expiry(timedelta(days=30))  # Session lasts for 30 days
                return redirect('home')  # Redirect to home after login
            else:
                messages.error(request, "Invalid username or password.")  # Show error message if authentication fails
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

# Signup View
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful signup
            return redirect('home')  # Redirect to home after signup
        else:
            messages.error(request, "Please correct the errors below.")  # Show errors if form is invalid
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/signup.html', {'form': form})

def password_reset(request):
    return render(request, 'users/password_reset.html')
