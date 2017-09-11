from django.shortcuts import render
from jobpost_app.models import Location
#from django.http import HttpResponse


# Create your views here.
def backend_location_view(request):
  template="jobpost_app/backend/location_list.html"
  locations=Location.objects.all()
  context={'title':'Job Location List','locs':locations}
  return render(request, template, context)