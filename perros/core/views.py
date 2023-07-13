from django.shortcuts import render, HttpResponse
from gestioncontactos.forms import FormularioContacto 

# Create your views here.
def home(request):
    #return HttpResponse("<h1>este es el home</h1>")
    return render(request, "core/home.html")
#def contacto(request):
#    return render(request, "core/contacto.html")
def contacto(request):
    if request.method=="POST": 
        miFormulario=FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            #Realizar operación con los datos aquí e incluir gracias.html
            return render(request,"core/gracias.html") 
    else:
        miFormulario=FormularioContacto()
    return render(request,"core/formulario_contacto.html",{"form":miFormulario})
def razas(request):
    return render(request, "core/razas.html")
def veterinarias(request):
    return render(request, "core/veterinarias.html")
