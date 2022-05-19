from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from familia.models import Persona


def listadoPersonas(self):
    lista = Persona.objects.all()
    diccionario = {'lista': lista}

    miHtml = open("C:/Users/agroppa/Desktop/py/MVTGroppa/MVTGroppa/plantillas/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    return HttpResponse (documento)