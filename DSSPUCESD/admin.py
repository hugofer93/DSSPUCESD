from django.contrib import admin

from DSSPUCESD import models

class AdminSite(admin.AdminSite):
	admin.AdminSite.site_header = "DSS Administrator"
	admin.AdminSite.site_title = "DSS Administrator"

@admin.register(models.Aprobacion)
class AdminPersona(admin.ModelAdmin):	
	class Meta:
		model = models.Aprobacion

@admin.register(models.Persona)
class AdminPersona(admin.ModelAdmin):
	list_display = ["cedula","nombre","apellido","telefono","email","estado"]
	list_display_link = ["cedula"]
	search_fields = ["cedula","nombre","apellido"]
	list_filter = ["estado"]
	ordering = ["nombre","apellido"]
	
	class Meta:
		model = models.Persona

@admin.register(models.ParamPrimario)
class AdminParamPrimario(admin.ModelAdmin):
	list_display = ["nombre","porcentaje"]
	list_display_link = ["nombre"]

	class Meta:
		model = models.ParamPrimario

@admin.register(models.ParamSecundario)
class AdminParamSecundario(admin.ModelAdmin):
	list_display = ["nombre","param_primario","porcentaje"]
	list_display_link = ["nombre"]

	class Meta:
		model = models.ParamSecundario

@admin.register(models.ParamTerciario)
class AdminParamTerciario(admin.ModelAdmin):
	list_display = ["nombre","param_secundario","porcentaje"]
	list_display_link = ["nombre"]
		
	class Meta:
		model = models.ParamTerciario