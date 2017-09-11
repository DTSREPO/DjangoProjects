from django.shortcuts import render

# Create your views here.
def home(request):
    template = 'employer_app/emp_dashboard.html'
    context = {'title': 'Employer'}
    return render(request, template, context)
