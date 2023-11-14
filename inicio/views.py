from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.template import loader
from inicio.models import Paleta, Auto, Moto
from inicio.forms import CrearPaletaFormulario, CrearMotoFormulario, CrearAutoFormulario

def inicio(request):
    
    #v2
    #template = loader.get_template('inicio.html')
    #template_renderizado = template.render({})
    
    #return HttpResponse(template_renderizado)
    
    #v3
    return render(request, 'inicio/inicio.html', {})


def paletas(request):
    
    marca_a_buscar = request.GET.get('marca')    
    
    if marca_a_buscar:
        listado_de_paletas = Paleta.objects.filter(marca__icontains = marca_a_buscar)
    else:
        listado_de_paletas = Paleta.objects.all()

    
    return render(request, 'inicio/paletas.html', {'listado_de_paletas': listado_de_paletas})

def autos(request):
    
    marca_a_buscar = request.GET.get('marca')    
    
    if marca_a_buscar:
        listado_de_autos = Auto.objects.filter(marca__icontains = marca_a_buscar)
    else:
        listado_de_autos = Auto.objects.all()

    
    return render(request, 'inicio/autos.html', {'listado_de_autos': listado_de_autos})

def motos(request):
    
    marca_a_buscar = request.GET.get('marca')    
    
    if marca_a_buscar:
        listado_de_motos = Moto.objects.filter(marca__icontains = marca_a_buscar)
    else:
        listado_de_motos = Moto.objects.all()

    
    return render(request, 'inicio/motos.html', {'listado_de_motos': listado_de_motos})

def crear_paleta(request):

    # if request.method == 'POST':
    #     marca = request.POST.get('marca')
    #     descripcion = request.POST.get('descripcion')
    #     anio = request.POST.get('anio')
    

    #     paleta = Paleta(marca=marca, descripcion=descripcion, anio=anio)
    #     paleta.save()
    
    if request.method == 'POST' :
        formulario = CrearPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            
            paleta = Paleta(marca=marca.lower(), descripcion=descripcion, anio=anio)
            paleta.save()
            
            return redirect('paletas')
        
        else:
            return render(request, 'inicio/crear_paleta.html', {'formulario' : formulario})
    
    formulario = CrearPaletaFormulario()
    return render(request, 'inicio/crear_paleta.html', {'formulario' : formulario})

def crear_auto(request):

    # if request.method == 'POST':
    #     marca = request.POST.get('marca')
    #     descripcion = request.POST.get('descripcion')
    #     anio = request.POST.get('anio')
    

    #     paleta = Paleta(marca=marca, descripcion=descripcion, anio=anio)
    #     paleta.save()
    
    if request.method == 'POST' :
        formulario = CrearAutoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            
            auto = Auto(marca=marca.lower(), modelo=modelo ,descripcion=descripcion, anio=anio)
            auto.save()
            
            return redirect('autos')
        
        else:
            return render(request, 'inicio/crear_autos.html', {'formulario' : formulario})
    
    formulario = CrearAutoFormulario()
    return render(request, 'inicio/crear_auto.html', {'formulario': formulario})

def crear_moto(request):

    # if request.method == 'POST':
    #     marca = request.POST.get('marca')
    #     descripcion = request.POST.get('descripcion')
    #     anio = request.POST.get('anio')
    

    #     paleta = Paleta(marca=marca, descripcion=descripcion, anio=anio)
    #     paleta.save()
    
    if request.method == 'POST' :
        formulario = CrearMotoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            
            moto = Moto(marca=marca.lower(), descripcion=descripcion, anio=anio)
            moto.save()
            
            return redirect('motos')
        
        else:
            return render(request, 'inicio/crear_moto.html', {'formulario' : formulario})
    
    formulario = CrearMotoFormulario()
    return render(request, 'inicio/crear_moto.html', {'formulario' : formulario})
# En tu vista de Django# Importa tu modelo de Auto

