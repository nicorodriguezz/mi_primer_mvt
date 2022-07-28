from multiprocessing import context
from django.shortcuts import render
from integrantes.models import integrantes


def define_integrante_1(request):
    integrante_1 = integrantes.objects.create(name="Oscar", last_name= "Denapoli", daily_work_hours= 6, pets= "no") 
    context = {
        "integrante_1" : integrante_1
    }
    return render(request, "integrante_1.html", context=context)

def define_integrante_2(request):
    integrante_2 = integrantes.objects.create(name="Santa", last_name= "De Luca", daily_work_hours= 4, pets= "no")
    context = {
        "integrante_2" : integrante_2
    }
    return render(request, "integrante_2.html", context=context)

def define_integrante_3(request):
    integrante_3 = integrantes.objects.create(name="Bianca", last_name= "Miglierini", daily_work_hours= 12, pets= "si")
    context = {
        "integrante_3" : integrante_3
    }
    return render(request, "integrante_3.html", context=context)    

def define_integrante_4(request):
    integrante_4 = integrantes.objects.create(name="Nicolas", last_name= "Rodriguez", daily_work_hours= 10, pets= "si")
    context = {
        "integrante_4" : integrante_4
    }
    return render(request, "integrante_4.html", context=context)


def full_integrantes(request):
    
    full_integrantes = integrantes.objects.all()
    context = {
        'full_integrantes': full_integrantes
    }
    return render(request, 'full_integrantes.html', context=context)