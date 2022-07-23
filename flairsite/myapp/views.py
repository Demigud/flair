from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Health
from .forms import CreateUserForm
from .forms import HealthForm
from django.contrib.auth.decorators import login_required



# Create your views here.

#Home
def home(request):
    return render(request, 'index.html')

#Login
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('healthform')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

    context={}
    return render(request, 'login.html', context)

#Register
def register(request):
    if request.user.is_authenticated:
        return redirect('healthform')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account ' + user + ' was created succesfully!')

                return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

#Need Login User Before Proceed
@login_required(login_url='login')
#HealthForm = CREATE
def healthform(request):
    form = HealthForm()
    if request.method == 'POST':
        form = HealthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('healthform')

    context={'form':form}        
    return render(request, 'health-form.html', context)

#Dashboard = UPDATE, DELETE
def dashboard(request):
    return render(request, 'dashboard.html')


def submissions(request):
    healthforms = Health.objects.all()

    context = {'healthforms': healthforms}
    return render(request, 'submissions.html', context)

def subupdate(request, id):
    health = Health.objects.get(id=id)
    form = HealthForm(initial={'name': health.name, 'email': health.email, 'phonenumber': health.phonenumber, 'address': health.address, 'temperature': health.temperature, 'choise1': health.choise1, 'travelhistory': health.travelhistory, 'choise2': health.choise2, 'choise3': health.choise3,})
    if request.method == 'POST':
        form = HealthForm(request.POST, instance=health)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('submissions')
            except Exception as e:
                pass

    context = {'form': form}
    return render(request, 'sub-update.html', context)

def subdelete(request, id):
    health = Health.objects.get(id=id)
    try:
        health.delete()
    except:
        pass

    return redirect('submissions')

def userlogs(request,):

    return render(request, 'user-logs.html')


def livefeed(request):

    return render(request, 'live-feed.html')