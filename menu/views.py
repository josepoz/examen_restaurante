from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Menu, Pedido
from .forms import MenuForm
from django.contrib import messages


# Create your views here.
def index(request):
    menus = Menu.objects.filter(fecha_registro__lte=timezone.now()).order_by('fecha_registro')
    return render(request, 'index.html', {'menus': menus})

def nuevo_menu(request):
    if request.method == "POST":
        formulario = MenuForm(request.POST)
        if formulario.is_valid():
            menu = Menu.objects.create(nombre=formulario.cleaned_data['nombre'], cocinero_responsable = formulario.cleaned_data['cocinero_responsable'], costo_total = formulario.cleaned_data['costo_total'])
            for plato_id in request.POST.getlist('platos'):
                pedido = Pedido(plato_id=plato_id, menu_id = menu.id, unidades=unidades)
                pedido.save()
            messages.add_message(request, messages.SUCCESS, 'Menu Guardado Exitosamente')
    else:
        formulario = MenuForm()
    return render(request, 'editar_menu.html', {'formulario': formulario})



# from django.shortcuts import render
# from django.contrib import messages
# from .forms import PeliculaForm
# from pelicula.models import Pelicula, Actuacion

# def pelicula_nueva(request):
#     if request.method == "POST":
#         formulario = PeliculaForm(request.POST)
#         if formulario.is_valid():
#             pelicula = Pelicula.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
#             for actor_id in request.POST.getlist('actores'):
#                 actuacion = Actuacion(actor_id=actor_id, pelicula_id = pelicula.id)
#                 actuacion.save()
#             messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
#     else:
#         formulario = PeliculaForm()
#     return render(request, 'pelicula/pelicula_editar.html', {'formulario': formulario})
