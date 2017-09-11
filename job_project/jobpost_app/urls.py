from django.conf.urls import include, url
from jobpost_app.views.index_view import (index_view)
from jobpost_app.views.backend_index_view import (backend_index_view)
from jobpost_app.views.backend_category_view import (backend_category_view)
from jobpost_app.views.backend_location_view import (backend_location_view)

urlpatterns = [
    url(r'^$', index_view, name='index'),
	
	#Backend Part
	url(r'^admin/$', backend_index_view, name='backend_index'),
	url(r'^admin/category/$', backend_category_view, name='cat-list'),
	url(r'^admin/location/$', backend_location_view, name='job-loc'),
]