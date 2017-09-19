from django.shortcuts import render
from jobpost_app.models import Location, Category
#from django.http import HttpResponse


# Create your views here.
def index_view(request):
  template="jobpost_app/frontend/index.html"
  locs=Location.objects.all()
  cats=Category.objects.all()
  context={'title':'Welcome To My Jobs Site', 'locs':locs, 'cats':cats}
  return render(request, template, context)