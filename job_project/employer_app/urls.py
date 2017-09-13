from django.conf.urls import include, url
from employer_app.views.index_view import index_view
from employer_app.views.employer_view import EmployerCrud, EmployerLoginReg





urlpatterns = [
    url(r'^dashboard/$', index_view, name='dashboard'),
    url(r'^login/$', EmployerLoginReg.as_view(), name='emp-login'),
	url(r'^update-profile/(?P<emp_id>[0-9]*)$', EmployerCrud.as_view(), name='upd-profile'),
]