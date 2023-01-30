from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=25)
    
    def __str__(self):
        return self.categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    precio = models.FloatField()
    stock = models.BooleanField()
    imagen = models.ImageField(upload_to=('productos/'))
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.nombre

