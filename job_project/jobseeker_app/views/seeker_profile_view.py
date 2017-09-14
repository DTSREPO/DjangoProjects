from django.shortcuts import render
from django.views import View
from jobseeker_app import models
#from jobpost_app.models import Industry

# Create your views here.
class SeekerLoginReg(View):
    template='jobseeker_app/seeker_login_reg.html'
    context={'title':'Jobs Seeker Login/Registration'}
	
    def get(self, request, seeker_id=None):
      return render(request, self.template, self.context)
	
    def post(self, request, seeker_id=None):
      first_name = request.POST.get('first_name','')
      last_name = request.POST.get('last_name','')
      gender = request.POST.get('gender','')
      mobile = request.POST.get('mobile','')
      email = request.POST.get('email','')
      industry_id = request.POST.get('industry','')
      user_name = request.POST.get('user_name','')
      user_pwd = request.POST.get('user_pwd','')
      re_pwd = request.POST.get('re-pwd','')
	  
	  
      if seeker_id:
        seeker=models.SeekerReg.objects.get(pk=seeker_id)
        seeker.first_name = first_name
        seeker.last_name = last_name
        seeker.gender = gender
        seeker.mobile = mobile
        seeker.email = email
        seeker.industry = industry_id
        seeker.save()
        msg="Data updated successfully ..."
      else:
        seeker=models.SeekerReg(
          first_name = first_name,
          last_name = last_name,
          gender = gender,
          mobile = mobile,
          email = email,
          user_name = user_name,
          user_pass = user_pwd
		)
        seeker.save()
        seeker.industry.add(industry_id)
        msg="Data saved successfully ..."
      context={'title':'Jobs Seeker Login/Registration','seeker':seeker,'msg':msg}
      return render(request, self.template, context)