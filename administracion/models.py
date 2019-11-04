from django.db import models
import django_filters

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=40)
    GENEROS_OPCIONES = (
            ('M','Masculino'),
            ('F','Femenino'),
            ('O','Otros'),
        )
    EC_OPCIONES = (
            ('S','Soltero'),
            ('C','Casado'),
            ('V','Viudo'),
            ('D','Divorciado'),
        )
    genero = models.CharField(max_length=1,choices=GENEROS_OPCIONES)
    foto = models.FileField(upload_to='myfolder/',blank=True,null=True)
    nacionalidad = models.CharField(max_length=100, default="Peru")
    fecha_nacimiento = models.DateField(blank=True,null=True)
    estado_civil = models.CharField(max_length=1,choices=EC_OPCIONES,default='S')
    #experienciaLaboral = models.ForeignKey(ExperienciaLaboral,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre+" "+self.apellidos

class Habilidades(models.Model):
    habilidad = models.CharField(max_length=100)
    NIVEL_OPCIONES = (
            ('P','Principiante'),
            ('I','Intermedio'),
            ('A','Avanzado'),
        )
    nivel = models.CharField(max_length=1,choices=NIVEL_OPCIONES,default='P')
    descripcion = models.TextField(null=True,blank=True)
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    def __str__(self):
        return self.habilidad

class Estudio(models.Model):
    titulo = models.CharField(max_length= 100)
    area_de_estudio = models.CharField(max_length=100)
    TIPO_ESTUDIO = (
            ('T','Tecnico'),
            ('U','Universitario'),
            ('M','Maestría'),
            ('D','Doctorado'),
            ('O','Otro'),
        )
    TIPO_ESTADO = (
            ('C','En curso'),
            ('G','Graduado'),
            ('A','Abandonado'),
        )
    tipoDeEstudio = models.CharField(max_length=1,choices=TIPO_ESTUDIO)
    estado = models.CharField(max_length=1,choices=TIPO_ESTADO)
    inicio = models.DateField()
    fin = models.DateField()
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo


class ExperienciaLaboral(models.Model):
    empresa = models.CharField(max_length=100)
    puesto = models.CharField(max_length=50)
    desde = models.DateField()
    hasta = models.DateField(blank=True, null=True)
    descripcion = models.TextField()
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE,default= False)
    def __str__(self):
        return self.empresa + " "+ self.puesto



class Document(models.Model):
    filename = models.CharField(max_length=100)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)

class AlumnoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Alumno
        fields =['nombre','dni']

class HabilidadFilter(django_filters.FilterSet):
    #nombre = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Habilidades
        fields = ['alumno__nombre']