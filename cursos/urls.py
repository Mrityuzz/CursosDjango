from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),
    path('crud/', views.lista_cursos, name='crud_cursos'),  
    path('agregar/', views.agregar_curso, name='agregar_curso'),
    path('editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('eliminar/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
]
