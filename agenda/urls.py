"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from agendaapp.views import index, cad_servico
from agendaapp.views import base03, base03

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('cad_servico/', cad_servico, name='cad_servico'),
    path ('base03/', base03, name='base03'),
]
