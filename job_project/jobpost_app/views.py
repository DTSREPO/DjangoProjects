from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.
def index(request):
  template="jobpost_app/index.html"
  context={'title':'Welcome'}
  return render(request, template, context)


def job_list(request):
  template="jobpost_app/joblist.html"
  context={'title':'Welcome to Jobs List'}
  return render(request, template, context)


def single_job(request):
  template="jobpost_app/single.html"
  context={'title':'Welcome to Single Job View'}
  return render(request, template, context)

def seeker_login(request):
  template="jobpost_app/seeker_login.html"
  context={'title':'Seeker Login / Regestration'}
  return render(request, template, context)
