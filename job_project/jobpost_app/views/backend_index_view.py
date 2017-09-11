from django.shortcuts import render
from jobpost_app.models import Location
#from django.http import HttpResponse


# Create your views here.
def backend_index_view(request):
  template="jobpost_app/backend/index.html"
  context={'title':'Jobpost Admin'}
  return render(request, template, context)