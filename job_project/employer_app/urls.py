from django.conf.urls import include, url
from employer_app.views.index_view import index_view
from employer_app.views.employer_view import employer_view

urlpatterns = [
    url(r'^$', index_view, name='home'),
]