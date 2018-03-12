from django.contrib import admin
from django.urls import path, include
from persona import views as views_persona

urlpatterns = [
    path('index', views_persona.index),
    #Personas
    path('crear/', views_persona.crear_persona),
    path('info/<int:persona_id>/', views_persona.info_persona),
    path('eliminar/persona/<int:persona_id>/', views_persona.eliminar_persona),
    path('modificar/persona/<int:persona_id>/', views_persona.modificar_persona),
    #Comentarios
    path('crear/comentario/', views_persona.crear_comentario_persona),
    path('info/<int:comentario_id>/', views_persona.info_comentario),
    path('eliminar/<int:comentario_id>/', views_persona.eliminar_comentario),
    path('modificar/comentario/<int:comentario_id>/', views_persona.modificar_comentario),
    #Rasgos
    path('crear/rasgo/', views_persona.crear_rasgo_persona),
    path('eliminar/<int:rasgo_id>/', views_persona.eliminar_rasgo),
]
