from django.shortcuts import render
from administracion.models import Alumno, Habilidades, Estudio, AlumnoFilter, HabilidadFilter
from django.http import HttpResponse
from django.template import loader
from datetime import date
# Create your views here.
def index(request):
	ultimos_alumnos = Alumno.objects.all()
	template = loader.get_template('empresa/index.html')
	context = {
		'ultimos_alumnos': ultimos_alumnos,
	}
	return HttpResponse(template.render(context, request ))

def calcular_edad(nacimiento):
	hoy = date.today()
	return hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month,nacimiento.day))

def detalle(request, alumno_id):
	try:
		alumno = Alumno.objects.get(pk=alumno_id)
		habilidades = Habilidades.objects.filter(alumno=alumno)
		estudios = Estudio.objects.filter(alumno=alumno)
		if (alumno.fecha_nacimiento):
			edad = calcular_edad(alumno.fecha_nacimiento)
		else:
			edad = 0
		context	= {
			'alumno': alumno,
			'lista_habilidades': habilidades,
			'estudios': estudios,
			'edad': edad,
		}
	except Alumno.DoesNotExist:
		raise Http404("Alumno no existe")
	return render(request,'empresa/detalle.html',context)

def filtro_alumnos(request):
	f = AlumnoFilter(request.GET, queryset = Alumno.objects.all())
	h = HabilidadFilter(request.GET, queryset = Habilidades.objects.all())
	return render(request,'empresa/filtro.html',{'filter':f,'habilidad':h})