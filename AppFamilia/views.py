from datetime import date
from AppFamilia.models import Familiar
from django.http import HttpResponse
from django.template import loader


def mama(request):
    fecha_nacimiento = date(1968,6,6)
    familiar = Familiar(parentesco = 'Madre',
                        edad = '60',
                        fecha_nacimiento = fecha_nacimiento)
    familiar.save()
    familiarDict = {'parentesco': familiar.parentesco,
                    'edad': familiar.edad,
                    'fecha_nacimiento': familiar.fecha_nacimiento}
    template = loader.get_template('madre.html')
    document =  template.render(familiarDict)
    return HttpResponse(document)

def papa(request):
    fecha_nacimiento = date(1960,10,30)
    familiar = Familiar(parentesco = 'Padre',
                        edad = '89',
                        fecha_nacimiento = fecha_nacimiento)
    familiar.save()
    familiarDict = {'parentesco': familiar.parentesco,
                    'edad': familiar.edad,
                    'fecha_nacimiento': familiar.fecha_nacimiento}
    template = loader.get_template('padre.html')
    document =  template.render(familiarDict)
    return HttpResponse(document)

def esposa(request):
    fecha_nacimiento = date(1987,6,7)
    familiar = Familiar(parentesco = 'Esposa',
                        edad = '35',
                        fecha_nacimiento = fecha_nacimiento)
    familiar.save()
    familiarDict = {'parentesco': familiar.parentesco,
                    'edad': familiar.edad,
                    'fecha_nacimiento': familiar.fecha_nacimiento}
    template = loader.get_template('esposa.html')
    document =  template.render(familiarDict)
    return HttpResponse(document)