from django.shortcuts import render
from jobpost_app.models import Location
#from django.http import HttpResponse


# Create your views here.
def index_view(request):
  template="jobpost_app/frontend/index.html"
  locs=Location.objects.all()
  context={'title':'Welcome To My Jobs Site', 'locs':locs}
  return render(request, template, context)