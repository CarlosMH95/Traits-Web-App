from django.contrib import admin
from django.urls import path, include
from persona import views as views_persona

urlpatterns = [
    path('index', views_persona.index, name="index"),
    #Personas
    path('crear/', views_persona.crear_persona, name="crear_p"),
    path('info/<int:persona_id>/', views_persona.info_persona, name="info_p"),
    path('eliminar/persona/<int:persona_id>/', views_persona.eliminar_persona, name="eliminar_p"),
    path('modificar/persona/<int:persona_id>/', views_persona.modificar_persona, name="mod_p"),
    #Comentarios
    path('crear/comentario/', views_persona.crear_comentario_persona),
    path('info/<int:comentario_id>/', views_persona.info_comentario),
    path('eliminar/<int:comentario_id>/', views_persona.eliminar_comentario),
    path('modificar/comentario/<int:comentario_id>/', views_persona.modificar_comentario),
    #Rasgos
    path('crear/rasgo/', views_persona.crear_rasgo_persona, name="crear_r"),
    path('eliminar/<int:rasgo_id>/', views_persona.eliminar_rasgo),
]
