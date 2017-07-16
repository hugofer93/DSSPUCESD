from django.views.generic import ListView, CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.utils.encoding import iri_to_uri
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from DSSPUCESD import models
from DSSPUCESD import forms

class Personal(ListView):
	model = models.Persona
	template_name = 'app/personal/personal.html'
	queryset = model.objects.order_by('-id').filter(estado=True)[:10]

class AgregarPersona(CreateView):
	model = models.Persona
	template_name = 'app/personal/agregar.html'
	form_class = forms.Form_Persona

	def form_valid(self, form):
		response = super(AgregarPersona, self).form_valid(form)
		# do something with self.object
		self.object.estado = True
		self.object.save()
		return response

	def get_success_url(self):
		return iri_to_uri(reverse('personal'))

class DetallePersona(UpdateView):
	model = models.Persona
	template_name = 'app/personal/detalle.html'
	pk_url_kwarg = 'id'
	form_class = forms.Form_Persona

	def form_valid(self, form):
		response = super(DetallePersona, self).form_valid(form)
		# do something with self.object
		if 'borrar' in self.request.POST:
			self.object.estado = False
			self.object.save()
		return response

	def get_success_url(self):
		return iri_to_uri(reverse('personal'))

class TodosPersonal(ListView):
	model = models.Persona
	paginate_by = 12
	template_name = 'app/personal/todos.html'
	queryset = model.objects.all().filter(estado = True)

	def post(self, request, *args, **kwargs):
		if 'borrar' in self.request.POST:
			obj = self.model.objects.get(id=self.request.POST['borrar'])
			obj.estado = False
			obj.save()
		return HttpResponseRedirect('')

class Concurso(ListView):
	model = models.Persona
	template_name = 'app/personal/personal.html'
	queryset = model.objects.order_by('-id').filter(estado=True)[:10]

class AgregarConcurso(TemplateView):
	template_name = 'app/concurso/agregar.html'
	
	def get_context_data(self, **kwargs):
		context = super(AgregarConcurso, self).get_context_data(**kwargs)
		parametros = Parametro
		context['parametro'] = parametros
		return context
	
	def post(self, request, *args, **kwargs):
		return HttpResponseRedirect('')

'''
class Prueba(TemplateView):
	template_name = 'app/prueba.html'

	def get_context_data(self, **kwargs):
		context = super(Prueba, self).get_context_data(**kwargs)
		context['nombre_pagina'] = 'Prueba'
		param_merito = ParamMerito
		context['ParamMerito'] = param_merito
		param_oposicion = ParamOposicion
		context['ParamOposicion'] = param_oposicion
		return context
'''
class Parametro:
	queryset = models.ParamTerciario.objects.all()
	titulo = queryset.filter(param_secundario__nombre = 'Titulos Profesionales')
	exp_aca = queryset.filter(param_secundario__nombre='Experiencia Academica')
	exp_inv = queryset.filter(param_secundario__nombre='Experiencia Investigativa')
	exp_pro = queryset.filter(param_secundario__nombre='Experiencia Profesional en el Area')
	premios = queryset.filter(param_secundario__nombre='Premios o Distinciones')
	publicaciones = queryset.filter(param_secundario__nombre='Publicaciones')
	participacion = queryset.filter(param_secundario__nombre='Participacion en Eventos Academicos')
	vinculacion = queryset.filter(param_secundario__nombre='Vinculacion con la Colectivada')
	entrevista = queryset.filter(param_secundario__nombre='Entrevista')
	prueba = queryset.filter(param_secundario__nombre='Pruebas')