from django.db import models

# Create your models here.
class Categoria(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    calificacion=models.IntegerField()

    def __str__(self):
        return self.name

class Pelicula(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    precio=models.IntegerField()
    duracion=models.IntegerField()
    descripcion=models.TextField()
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.name