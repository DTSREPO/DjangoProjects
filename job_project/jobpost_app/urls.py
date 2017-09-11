from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^job-list/$', views.job_list, name='job_list'),
    url(r'^single-job/$', views.single_job, name='single-job'),
]