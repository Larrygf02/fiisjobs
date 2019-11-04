from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


from .import views

urlpatterns = [
	url(r'^$',views.my_view,name='my_view'),
	url(r'^archivos/$',views.upload_file,name='file'),
]
