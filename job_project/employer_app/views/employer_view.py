from django.shortcuts import render
from django.views import View
from employer_app import models
#from jobpost_app.models.industry import Industry

# Create your views here.
'''
def employer_dashboard_view(request):
    template = 'employer_app/index.html'
    context = {'title': 'Employer'}
    return render(request, template, context)


def emp_profile_update_view(request):
  template = 'employer_app/edit_employer_profile.html'
  context = {'title': 'Edit Employer Profile'}
  return render(request, template, context)
'''

class EmployerCrud(View):

  template = 'employer_app/edit_employer_profile.html'
  #industries = models.Industry.objects.all()
  
  def get(self, request, emp_id=None):
    emp=models.Employer.objects.get(pk=1)
    #context = {'title': 'Edit Employer Profile','emp':emp, 'industries':self.industries}
    context = {'title': 'Edit Employer Profile','emp':emp}
    return render(request, self.template, context)
    
  def post(self, request, emp_id=None):
    #user_name =
    #user_pass =
    company_name = request.POST['com_name']
    #contact_person = request.POST['']
    #industry_type	= 
    #country = 
    #city = 
    company_address = request.POST['com_address']
    billing_address = request.POST['billing_address']
    contact_phone = request.POST['contact_phone']
    contact_email = request.POST['contact_email']
    website = request.POST['website']
	
    if emp_id:
      emp=models.Employer.objects.get(pk=emp_id)
      emp.company_name = company_name
      emp.company_address = company_address
      emp.billing_address = billing_address
      emp.contact_phone = contact_phone
      emp.contact_email = contact_email
      emp.website = website
      emp.save()
    else:
      emp=models.Employer(
        company_name = company_name,
	    company_address = company_address,
	    billing_address = billing_address,
	    contact_phone = contact_phone,
	    contact_email = contact_email,
	    website = website
	  )
      emp.save()
	  
    context={'title': 'Edit Employer Profile','emp':emp}
    return render(request, self.template, context)