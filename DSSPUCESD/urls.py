"""DSSPUCESD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required

from DSSPUCESD import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',TemplateView.as_view(template_name='index/index.html'), name='index'),
    url(r'^login/$', login, {'template_name': 'login/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^inicio/$', login_required(TemplateView.as_view(template_name='app/inicio.html')), name='inicio'),
    
    #PERSONAL
    url(r'^personal/$', login_required(views.Personal.as_view()), name='personal'),
    url(r'^agregar/persona/$',login_required(views.AgregarPersona.as_view()), name='agregar_persona'),
    url(r'^persona/id/(?P<id>\d+)$',login_required(views.DetallePersona.as_view()), name='detalle_persona'),
    url(r'^personal/todos/$', login_required(views.TodosPersonal.as_view()), name='todos_personal'),
    
    #CONCURSO
    url(r'^concurso$', login_required(TemplateView.as_view(template_name='app/concurso/concurso.html')), name='concurso'),
    url(r'^agregar/concurso$', login_required(views.AgregarConcurso.as_view()), name='agregar_concurso'),
    #url(r'^prueba$',views.Prueba.as_view())
    #url(r'^concurso/$',, name='concurso'),
    #url(r'^concurso/agregar$',, name='concurso_agregar'),
    #url(r'^concurso/resultado$',, name='concurso_resultado'),
]
