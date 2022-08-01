from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Health
from .forms import CreateUserForm
from .forms import HealthForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.files.uploadedfile import SimpleUploadedFile



# Create your views here.

#Home
@login_required(login_url='login')
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
        form = HealthForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('healthform')

    context={'form':form}        
    return render(request, 'health-form.html', context)

#Dashboard = UPDATE, DELETE
@user_passes_test(lambda user: user.is_staff, login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

@user_passes_test(lambda user: user.is_staff, login_url='login')
def submissions(request):
    healthforms = Health.objects.all()

    context = {'healthforms': healthforms}
    return render(request, 'submissions.html', context)

@user_passes_test(lambda user: user.is_staff, login_url='login')
def subdelete(request, id):
    health = Health.objects.get(id=id)
    try:
        health.delete()
    except:
        pass

    return redirect('submissions')

@user_passes_test(lambda user: user.is_staff, login_url='login')
def userlogs(request):
    userforms = get_user_model().objects.all()

    context = {'userforms': userforms}
    return render(request, 'user-logs.html', context)

@user_passes_test(lambda user: user.is_staff, login_url='login')
def userdelete(request, id):
    userform = get_user_model().objects.get(id=id)
    try:
        userform.delete()
    except:
        pass

    return redirect('userlogs')

@user_passes_test(lambda user: user.is_staff, login_url='login')
def livefeed(request):

    return render(request, 'live-feed.html')

def testform(request):
    form = HealthForm()
    if request.method == 'POST':
        form = HealthForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('healthform')

    context={'form':form}        
    return render(request, 'test-form.html', context)