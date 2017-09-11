from django.conf.urls import include, url
from employer_app.views.index_view import index_view
from employer_app.views.employer_view import employer_view, emp_profile_update_view





urlpatterns = [
    url(r'^dashboard/$', index_view, name='dashboard'),
    url(r'^update-profile/', emp_profile_update_view, name='upd-profile'),
]