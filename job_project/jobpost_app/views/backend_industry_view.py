from django.shortcuts import render
from jobpost_app.models import Industry
from django.views import View


# Create your views here.
def backend_industry_view(request):
  template="jobpost_app/backend/industry_list.html"
  inds=Industry.objects.filter(active=True)
  context={'title':'Industry List', 'inds':inds}
  return render(request, template, context)

class IndustryCrud(View):
  template="jobpost_app/backend/industry_form.html"
  
  def get(self, request, ind_id=None):
    if ind_id:
      ind=Industry.objects.get(pk=ind_id)
      context={'ind':ind}
      return render(request, self.template, context)
    else:
      return render(request, self.template)
	
  def post(self, request, ind_id=None):
    name=request.POST.get('name','')
    slug=request.POST.get('slug','')
    desc=request.POST.get('description','')
    #status=request.POST.get('status','')
	
    if ind_id:
      ind=Industry.objects.get(pk=ind_id)
      ind.name=name
      ind.slug=slug.lower()
      ind.description=desc
      #ind.active=status
      ind.save()
      msg='Data Updated Successfully'
    else:
      ind = Industry(
        name = name,
        slug = slug.lower(),
        description = desc
        #active = status	  
	  )
      ind.save()
      msg='Data Inserted Successfully'
    context={'ind':ind, 'msg':msg}
    return render(request, self.template, context)