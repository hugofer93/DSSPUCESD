from django.core.urlresolvers import reverse
from django.utils.encoding import iri_to_uri

from django.db import models

class Persona(models.Model):
	nombre = models.CharField(max_length=45)
	apellido = models.CharField(max_length=45)
	cedula = models.CharField(max_length=10)
	direccion = models.CharField(max_length=80)
	telefono = models.CharField(max_length=45)
	email = models.EmailField(max_length=30)
	estado = models.BooleanField(default=True)

	estado.boolean = True

	def __str__(self):
		return (self.nombre+" "+self.apellido+" "+self.cedula)

	class Meta:
		ordering = ["nombre","apellido"]
		verbose_name="persona"
		verbose_name_plural="Personas"

	def get_absolute_url(self):
		return iri_to_uri(reverse('detalle_persona', args = [str(self.id)]))

class Aprobacion(models.Model):
	porcentaje = models.DecimalField(max_digits = 4, decimal_places = 2)
	
	def __str__(self):
		return str(self.porcentaje)
	
	class Meta:
		ordering = ["id"]
		verbose_name="Aprobacion"
		verbose_name_plural="Aprobacion"
	
class ParamPrimario(models.Model):
	nombre = models.CharField(max_length=50)
	porcentaje = models.DecimalField(max_digits = 4, decimal_places = 2)
	
	def __str__(self):
		return (self.nombre)
	
	class Meta:
		ordering = ["id"]
		verbose_name="parametro primario"
		verbose_name_plural="parametros primarios"
	
class ParamSecundario(models.Model):
	param_primario = models.ForeignKey(ParamPrimario)
	nombre = models.CharField(max_length=50)
	porcentaje = models.DecimalField(max_digits = 4, decimal_places = 2)
	
	def __str__(self):
		return (self.nombre)
	
	class Meta:
		ordering = ["id"]
		verbose_name="parametro secundario"
		verbose_name_plural="parametros secundarios"
	
class ParamTerciario(models.Model):
	param_secundario = models.ForeignKey(ParamSecundario)
	nombre = models.CharField(max_length=50)
	porcentaje = models.DecimalField(max_digits = 4, decimal_places = 2)
	
	def __str__(self):
		return (self.nombre)
	
	class Meta:
		ordering = ["id"]
		verbose_name="parametro terciario"
		verbose_name_plural="parametros terciarios"

class Concurso(models.Model):
	persona = models.OneToOneField(Persona)
	