from django.shortcuts import render

# Create your views here.
def employer_view(request):
    template = 'employer_app/index.html'
    context = {'title': 'Employer'}
    return render(request, template, context)


def emp_profile_update_view(request):
    template = 'employer_app/edit_employer_profile.html'
    context = {'title': 'Edit Employer Profile'}
    return render(request, template, context)
