from django.shortcuts import render
from django.views import View

# Create your views here.



class SeekerLoginReg(View):
    template='jobseeker_app/seeker_login_reg.html'
    def get(self, request, user_id=None):
      return render(request, self.template, context={'title':'Jobs Seeker Login/Registration'})