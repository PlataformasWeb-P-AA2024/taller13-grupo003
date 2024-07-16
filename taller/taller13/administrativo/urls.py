"""
URL configuration for waveForex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('edificios/<int:id>', views.obtener_edificio,name = 'obtener_edificio'),
    path('crear/edificios', views.crear_edificio,name='crear_edificio'),
    path('editar/edificios/<int:id>', views.editar_edificio,name='editar_edificio'),
    path('eliminar/edificios/<int:id>', views.eliminar_edificio,name='eliminar_edificio'),

    path('crear/departamento', views.crear_departamento,name='crear_departamento'),
    path('editar/departamento/<int:id>', views.editar_departamento,name='editar_departamento'),
    path('eliminar/departamento/<int:id>', views.eliminar_departamento,name='eliminar_departamento'),

    path('crear/departamento/edificio/<int:id>', views.crear_departamento_edificio,
            name='crear_departamento_edificio'),

    path('saliendo/logout/', views.logout_view, name="logout_view"),
    path('entrando/login/', views.ingreso, name="login"),
]