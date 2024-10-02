from django.shortcuts import render

def home_view(request):
    return render(request, 'home/home.html')

def features(request):
    return render(request, 'home/features.html')

def how_it_works(request):
    return render(request, 'home/how_it_works.html')

def contact(request):
    return render(request, 'home/contact.html')
