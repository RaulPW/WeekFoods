from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_compra, name='Lista Compra'),

]