from django.shortcuts import render

# Create your views here.
def home(request):
    template = 'admin_app/admin_dashboard.html'
    context = {'title': 'Jobs Amin Panel'}
    return render(request, template, context)
