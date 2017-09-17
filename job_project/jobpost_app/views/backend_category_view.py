from django.shortcuts import render
from jobpost_app.models import Category
from django.views import View


# Create your views here.
def backend_category_view(request):
  template="jobpost_app/backend/category_list.html"
  cats=Category.objects.filter(active=True)
  context={'title':'Category List', 'cats':cats}
  return render(request, template, context)

class CategoryCrud(View):
  template="jobpost_app/backend/category_form.html"
  
  def get(self, request, cat_id=None):
    if cat_id:
      cat=Category.objects.get(pk=cat_id)
      context={'title':'Category Form', 'cat':cat}
      return render(request, self.template, context)
    else:
      return render(request, self.template, {'title':'Category Form'})
	
  def post(self, request, cat_id=None):
    name=request.POST.get('name','')
    slug=request.POST.get('slug','')
    desc=request.POST.get('description','')
    #status=request.POST.get('status','')
	
    if cat_id:
      cat=Category.objects.get(pk=cat_id)
      cat.name=name
      cat.slug=slug.lower()
      cat.description=desc
      #cat.active=status
      cat.save()
      msg='Data Updated Successfully'
    else:
      cat = Category(
        name = name,
        slug = slug.lower(),
        description = desc
        #active = status	  
	  )
      cat.save()
      msg='Data Inserted Successfully'
    context={'title':'Category Form', 'cat':cat, 'msg':msg}
    return render(request, self.template, context)