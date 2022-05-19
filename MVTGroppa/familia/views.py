from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template import loader
from familia.models import Persona


def listadoPersonas(self):
    lista = Persona.objects.all()
    diccionario = {'lista': lista}

    
    plantilla = loader.get_template('template1.html')



    documento = plantilla.render(diccionario)

    return HttpResponse (documento)