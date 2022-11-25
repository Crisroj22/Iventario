from django.db import models
from django.contrib.auth.models import User
class usuario(models.Model):
    bodeguero = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    
class Categoria(models.Model):
    marca = models.CharField(max_length=30, verbose_name='Marca')
    fabricante = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return self.marca
    

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    SKU = models.CharField(max_length=30, unique=True)
    stock = models.IntegerField(default=0, verbose_name='Stock')
    cod_producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    faltante = models.IntegerField(default=0,null=True, blank=True)
    vendido = models.IntegerField(default=0,null=True, blank=True)
    descuento = models.CharField(max_length=50,null=True, blank=True)
    valor_unitario = models.CharField(max_length=50,null=True, blank=True)
    cat = models.ForeignKey(Categoria, on_delete= models.CASCADE, null=True, blank=True)
   
     
    
    
        
           

   

