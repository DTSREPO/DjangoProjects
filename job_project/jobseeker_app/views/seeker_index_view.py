from django.shortcuts import render
from django.views import View

# Create your views here.


def seeker_index_view(request):
    template='jobseeker_app/seeker_dashboard.html'
    context = {'title':'Dashboard','sub_title':'Overview'}
    return render (request, template, context)