# practing this project in git hub
from django.shortcuts import render
from jobsapp.models import *

# Create your views here.
def homepage_view(request):
    print("Hello github")
    return render(request,'jobsapp/index.html')

def hydjobs_view(request):
    jobs_list= HydJobs.objects.all()
    type = 'Hyderabad'
    mydict= {'jobs_list':jobs_list, 'type':type}
    return render(request,'jobsapp/jobs.html',mydict)

def chennaijobs_view(request):
    jobs_list= ChennaiJobs.objects.all()
    type = 'Chennai'
    mydict= {'jobs_list':jobs_list, 'type':type}
    return render(request,'jobsapp/jobs.html',mydict)

def bglrjobs_view(request):
    jobs_list= BglrJobs.objects.all()
    type = 'Bangalore'
    mydict= {'jobs_list':jobs_list, 'type':type}
    return render(request,'jobsapp/jobs.html',mydict)

def punejobs_view(request):
    jobs_list= PuneJobs.objects.all()
    type = 'Pune'
    mydict= {'jobs_list':jobs_list, 'type':type}
    return render(request,'jobsapp/jobs.html',mydict)
