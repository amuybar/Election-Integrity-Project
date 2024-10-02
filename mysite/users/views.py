# user/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
                return redirect('home')  # Redirect to home after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')  # Redirect to login after signup
    else:
        form = UserCreationForm()

    return render(request, 'users/signup.html', {'form': form})

def password_reset(request):
    return render(request, 'users/password_reset.html')