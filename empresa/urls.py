
from django.conf.urls import url

from .import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^(?P<alumno_id>[0-9]+)/$',views.detalle,name='detalle'),
	url(r'^list$',views.filtro_alumnos,name='filtro'),
]
