from django.shortcuts import render
from jobpost_app.models.category import Category
# Create your views here.
def home(request):
  template = 'jobpost_app/seeker_login.html'
  cats=Category.objects.all()
  context = {'title': 'Job Seeker Login / Reg','cat':cats}
  return render(request, template, context)
