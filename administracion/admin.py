from django.contrib import admin
from .models import Alumno, ExperienciaLaboral, Habilidades, Estudio
# Register your models here.


class ExperienciaLaboralInline(admin.StackedInline):
	model = ExperienciaLaboral
	extra = 1

class HabilidadInline(admin.StackedInline):
	model = Habilidades
	extra = 1

class EstudioInline(admin.StackedInline):
	model = Estudio
	extra = 1

class AlumnoAdmin(admin.ModelAdmin):
	inlines = [ExperienciaLaboralInline,HabilidadInline,EstudioInline]

admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(ExperienciaLaboral)
#admin.site.register(Document)