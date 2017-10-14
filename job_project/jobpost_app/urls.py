




from django.conf.urls import include, url
from jobpost_app.views.index_view import (index_view)
from jobpost_app.views.backend_index_view import (backend_index_view)
from jobpost_app.views.backend_category_view import (backend_category_view, CategoryCrud)
from jobpost_app.views.backend_industry_view import (backend_industry_view, IndustryCrud)
from jobpost_app.views.backend_location_view import (backend_location_view, LocationCrud)

urlpatterns = [
	#Frontend Part
    url(r'^$', index_view, name='index'),
	
	#Backend Part
	url(r'^admin/dashboard/$', backend_index_view, name='backend_index'),
	url(r'^admin/category/$', backend_category_view, name='cat-list'),
	url(r'^admin/category-form/(?P<cat_id>[0-9]*)$', CategoryCrud.as_view(), name='cat-form'),
	url(r'^admin/industry/$', backend_industry_view, name='ind-list'),
	url(r'^admin/industry-form/(?P<ind_id>[0-9]*)$', IndustryCrud.as_view(), name='ind-form'),
	url(r'^admin/location/$', backend_location_view, name='job-loc'),
	url(r'^admin/location-form/(?P<loc_id>[0-9]*)$', LocationCrud.as_view(), name='loc-form'),
]