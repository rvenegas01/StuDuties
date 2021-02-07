from django.http import HttpResponse
from django.template import Template, Context
import datetime

def initi(request):
    return HttpResponse("prueba de la pirmera vista")

def date(request):
    fecha = datetime.datetime.now()
    doc = """<html>
     <body>
     <h1>
     Fecha-hora actual: %s
     </h1>
     <body>
    </html> 
     """ % fecha

    return HttpResponse(doc)

def edad(request, anio, anio_act, edad):

    s = anio-anio_act
    edads = s+edad

    doc = "<html><body><h1>En el año %s tendrás %s</h1><body></html>" %(anio, edads)

    return HttpResponse(doc)

def test(request):

    doc = open("C:/Users/risaa/OneDrive/Escritorio/Proyecto StuDuties/StuDuties/StuDuties/templates/test.html")

    tmplt = Template(doc.read())

    doc.close()

    cntx = Context()

    documento = tmplt.render(cntx)

    return HttpResponse(documento)