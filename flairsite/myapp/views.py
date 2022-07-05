from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#Home
def home(request):
    return render(request, 'index.html')

#Login
def login(request):
    return render(request, 'login.html')

#Register
def register(request):
    return render(request, 'register.html')

#HealthForm
def healthform(request):
    return render(request, 'health-form.html')