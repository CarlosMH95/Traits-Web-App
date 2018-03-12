from django.shortcuts import render, get_object_or_404
from .models import Persona, Rasgos, Comentarios, comentariosForm, personaForm

'''
    Modulo de personas y rasgos

    Version 0.1.0

    Actualizado 08/03/2018

'''
# Create your views here.
def index(request):
    personas = Persona.objects.all()
    data = {
        'personas':personas
    }
    template = 'persona/index.html'
    return render(request, template, data)
'''
Funcion:    crear_persona
Entradas:   Requerimiento GET o POST
Salidas:    Template para la renderizacion del formulario de ingreso de personas,
            o mensaje de ingreso exitoso/fallido
'''
def crear_persona(request):
    template = 'persona/index.html'
    form = personaForm(request.POST, request.FILES)
    if form.is_valid():
        '''
        Si se recibe el formulario en un POST, se realiza la validacion y el guardado
        del formulario.
        '''
        persona=form.save(commit=False)
        return render(request, template, {'msg':'Persona creada con exito'})
    else:
        print(form._errors)
    context = {
        "form":form,
    }
    return render(request,'persona/form_persona.html', context)

def eliminar_persona(request, persona_id):
    persona=Persona.objects.get(pk=paciente_id)
    persona.delete()
    return render(request, 'persona/index.html', {'msg':'Persona eliminada con éxito'})

def info_persona(request, persona_id):
    persona = get_object_or_404(Persona,pk=persona_id)
    return render(request, 'persona/perfil.html', {'persona':persona})
    

def modificar_persona(request, persona_id):
    try:
        persona = get_object_or_404(Persona, pk=persona_id)
    except:
        context={
            'msg':'No se encontro personal con el ID'
        }
        return (request, 'persona/index.html', context)
    
    pass

def crear_rasgo_persona(request):
    pass

def crear_comentario_persona(request):
    pass

def eliminar_rasgo(request):
    pass

def eliminar_comentario(request, comentario_id):
    pass
    
def info_comentario(request, comentario_id):
    pass

def modificar_comentario(request, comentario_id):
    pass

