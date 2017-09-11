from django.shortcuts import render
from jobpost_app.models import Category
#from django.http import HttpResponse


# Create your views here.
def backend_category_view(request):
  template="jobpost_app/backend/category_list.html"
  cats=Category.objects.all()
  context={'title':'Category List', 'cats':cats}
  return render(request, template, context)