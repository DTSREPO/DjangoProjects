from django.shortcuts import render
from django.views import View
from employer_app import models as EmpModels
from jobpost_app import models as JobModels

# Create your views here.

class EmployerLoginReg(View):
    template='employer_app/employer_login_reg.html'
    def get(self, request, emp_id=None):
      return render(request, self.template, context={'title':'Employer Login/Registration'})

class EmployerCrud(View):

  template = 'employer_app/edit_employer_profile.html'
  industries = JobModels.Industry.objects.all()
  
  def get(self, request, emp_id=None):
    if emp_id:
      emp = EmpModels.Employer.objects.get(pk=1)
      context = {'title': 'Edit Employer Profile','emp':emp, 'industries':self.industries}
      return render(request, self.template, context)
    else:
      return render(request, self.template)
    
  def post(self, request, emp_id=None):
    #user_name =
    #user_pass =
    company_name = request.POST['com_name']
    #contact_person = request.POST['']
    industry_type = request.POST.getlist('industry_type')
    #country = 
    #city = 
    company_address = request.POST['com_address']
    billing_address = request.POST['billing_address']
    contact_phone = request.POST['contact_phone']
    contact_email = request.POST['contact_email']
    website = request.POST['website']
	
    industries =[]
    for ind_id in industry_type:
      inds=JobModels.Industry.objects.get(pk=ind_id)
      industries.append(inds)
		
	
	
    if emp_id:
      emp=EmpModels.Employer.objects.get(pk=emp_id)
      emp.company_name = company_name
      emp.company_address = company_address
      emp.billing_address = billing_address
      emp.contact_phone = contact_phone
      emp.contact_email = contact_email
      emp.website = website
      emp.industry_type = industries
      emp.save()
    else:
      emp=EmpModels.Employer(
        company_name = company_name,
	    company_address = company_address,
	    billing_address = billing_address,
	    contact_phone = contact_phone,
	    contact_email = contact_email,
	    website = website
	  )
      emp.save()
      emp.industry_type.add(*industries)
	  
    context={'title': 'Edit Employer Profile','emp':emp, 'industries':self.industries}
    return render(request, self.template, context)
	
	
	
	
	