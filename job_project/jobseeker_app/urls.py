from django.conf.urls import include, url
from jobseeker_app.views.seeker_index_view import seeker_index_view
from jobseeker_app.views.seeker_profile_view import SeekerLoginReg

urlpatterns = [
	url(r'^dashboard/$', seeker_index_view, name='dashboard'),
    url(r'^login/$', SeekerLoginReg.as_view(), name='seeker-login'),
]