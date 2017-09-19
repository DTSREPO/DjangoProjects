from django.shortcuts import render
from django.views import View
from employer_app import models as EmpModels
from jobpost_app import models as JobModels

# Create your views here.

class JobPostCrud(View):
    template = 'employer_app/job_post_form.html'
    industries = JobModels.Industry.objects.all()
    categories = JobModels.Category.objects.all()
    locations = JobModels.Location.objects.all()
    emp = EmpModels.Employer.objects.get(pk=1)
	
    def get(self, request, job_id=None):

      if job_id:
        jobpost = EmpModels.JobPost.objects.get(pk=job_id)
        context = {
          'title':'Create or Update Job Post',
          'emp':self.emp, 'industries':self.industries,
          'categories':self.categories,
          'locations':self.locations,
          'jobpost':jobpost
		}
        return render(request, self.template, context)
      else:
        context = {
          'title':'Create or Update Job Post',
          'emp':self.emp, 'industries':self.industries,
          'categories':self.categories,
          'locations':self.locations
		}
        return render(request, self.template, context)

    def post(self, request, job_id=None):
	  
      com_id = request.POST.get('com-id')
      category = request.POST.get('category')
      industry = request.POST.get('industry')
      job_title = request.POST.get('job-title','')
      vacancies = request.POST.get('vacancies','')
      attach_photo = request.POST.get('attach-photo','')
	  
      if job_id:
        jobpost = EmpModels.JobPost.objects.get(pk=job_id)
		
        jobpost.company_id = com_id
        jobpost.category_id = category
        jobpost.industry_id = industry
        jobpost.job_title = job_title
        jobpost.vacancies = vacancies
        jobpost.with_photo = attach_photo
        jobpost.save()
		
        context = {
          'title':'Create or Update Job Post',
          'emp':self.emp, 'industries':self.industries,
          'categories':self.categories,
          'locations':self.locations,
          'jobpost':jobpost,
		  'msg':'Job Updated!'
		}
        return render(request, self.template, context)
		
      else:
        jobpost=EmpModels.JobPost(
          company_id = com_id,
          category_id = category,
          industry_id = industry,
          job_title = job_title,
          vacancies = vacancies,
          with_photo = attach_photo
        )
        jobpost.save()
        context = {
          'title':'Create or Update Job Post',
          'emp':self.emp, 'industries':self.industries,
          'categories':self.categories,
          'locations':self.locations,
          'jobpost':jobpost,
		  'msg':'New Job Inserted!'
		}
        return render(request, self.template, context)