from django.shortcuts import render
from employer_app import models as JobPostModels

# Create your views here.
def index_view(request):
    template = 'employer_app/index.html'
    jobs = JobPostModels.JobPost.objects.all()
    context = {
      'title': 'Dashboard',
      'sub_title':'Application List',
      'jobs':jobs
	}
    return render(request, template, context)
