from django.db import models
from django.forms import ModelForm
from django.forms import TextInput, DateInput

# Create your models here.

class Persona(models.Model):
    #Opciones
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    )
    #Informacion general de la persona
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    genero = models.CharField(max_length=1, choices=GENERO)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    fecha_actualizado = models.DateField(auto_now=True)
    foto = models.ImageField(blank=True)

#Modelo que manejara los traits
class Rasgos(models.Model):
    #Opciones
    # CARACTERISTICAS = (
    #     ('comun','Comun'),
    #     ('indiv','Individual'),
    #     ('centr','Central'),
    #     ('secun','Secundario'),
    #     ('cardi','Cardinal')
    # )
    TIPO = (
        ('POSI','Positivo'),
        ('NEGA','Negativo'),
        ('NEUT','Neutral'),
    )

    # caracteristicas = models.CharField(max_length=5, choices=CARACTERISTICAS)
    tipo = models.CharField(max_length=4, choices=TIPO)
    nombre = models.CharField(max_length= 100, default=None)
    persona = models.ForeignKey(
        'Persona',
        on_delete = models.CASCADE,
    )


class Comentarios(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(max_length=500)
    img = models.ImageField()
    persona = models.ForeignKey(
        'Persona',
        on_delete = models.CASCADE,
    )
    confirmado = models.BooleanField()

##################################################################################
##                      FORMS CREADOS DE LOS MODELOS                            ##
##################################################################################


class personaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'fecha_nacimiento' : DateInput(),
        }

class comentariosForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = ['titulo', 'contenido', 'img', 'confirmado']

class rasgosForm(ModelForm):
    class Meta:
        model = Rasgos
        fields='__all__'