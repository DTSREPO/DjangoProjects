from django.shortcuts import render


# Create your views here.
def index_view(request):
    template = 'employer_app/index.html'
    context = {'title': 'Job Application List'}
    return render(request, template, context)
