from django.shortcuts import render
from jobpost_app.models import Location
from django.views import View


# Create your views here.
def backend_location_view(request):
  template="jobpost_app/backend/location_list.html"
  locations=Location.objects.filter(active=True)
  context={'title':'Job Location List','locs':locations}
  return render(request, template, context)

  
class LocationCrud(View):
  template="jobpost_app/backend/location_form.html"
  
  def get(self, request, loc_id=None):
    if loc_id:
      loc=Location.objects.get(pk=loc_id)
      context={'loc':loc}
      return render(request, self.template, context)
    else:
      return render(request, self.template)
	
  def post(self, request, loc_id=None):
    name=request.POST.get('name','')
    slug=request.POST.get('slug','')
    desc=request.POST.get('description','')
    #status=request.POST.get('status','')
	
    if loc_id:
      loc=Location.objects.get(pk=loc_id)
      loc.name=name
      loc.slug=slug.lower()
      loc.description=desc
      #loc.active=status
      loc.save()
      msg='Data Updated Successfully'
    else:
      loc = Location(
        name = name,
        slug = slug.lower(),
        description = desc
        #active = status	  
	  )
      loc.save()
      msg='Data Inserted Successfully'
    context={'loc':loc, 'msg':msg}
    return render(request, self.template, context)