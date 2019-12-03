from django.shortcuts import render
from .models import Categoria,Pelicula #importar los modelos desde el archivo models.py
# Create your views here.
def index(request):
    return render(request,'core/index.html')

def gale(request):
    return render(request,'core/galeria.html')

def formulario(request):
    categorias=Categoria.objects.all() # select * form Categoria
    if request.POST:
        # recuperar el valor del boton accion
        accion=request.POST.get("accion")
        if accion=='grabar':            
            titulo=request.POST.get("txtTitulo")
            precio=request.POST.get("txtPrecio")
            duracion=request.POST.get("txtDuracion")
            descrip=request.POST.get("txtDescripcion")
            catego=request.POST.get("cboCategoria")
            obj_categoria=Categoria.objects.get(name=catego)
            #instanciar un objeto (modelo) Pelicula
            peli=Pelicula(
                name=titulo,
                precio=precio,
                duracion=duracion,
                descripcion=descrip,
                categoria=obj_categoria
            )
            peli.save() #graba los datos del modelo
            return render(request,'core/formulario.html',{'listacategoria':categorias,'msg':'grabo'})
        if accion=='eliminar':
            titulo=request.POST.get("txtTitulo")#recupera el titulo
            peli=Pelicula.objects.get(name=titulo)# lo busca entre las peliculas
            peli.delete()#elimina
            return render(request,'core/formulario.html',{'listacategoria':categorias,'msg':'elimino'})
    return render(request,'core/formulario.html',{'listacategoria':categorias})

def quienes_somos(request):
    return render(request,'core/quienes_somos.html')