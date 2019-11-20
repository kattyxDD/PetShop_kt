from django.db import models
from django.utils import timezone



class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200)
    apellidos = models.CharField(max_length = 255)
    edad = models.IntegerField()
    telefono = models.CharField(max_length = 12)


class Producto(models.Model):
    PERRO = 'Perro'
    GATO = 'Gato'
    ERIZO = 'Erizo'
    OTRO = 'Otro'
    ANIMAL_CHOICES = ((PERRO, 'Perro'),(GATO, 'Gato'),(ERIZO, 'Erizo'),(OTRO, 'Otro'))

    COLLAR = 'Collar'
    Limpieza = 'Limpieza'
    ROPA = 'Ropa'
    PRODUCT_CHOICES = ((COLLAR, 'Collar'),(Limpieza, 'Limpieza'),(ROPA, 'Ropa'))

   
    id = models.AutoField(primary_key = True)
    animal = models.CharField(max_length=20, choices=ANIMAL_CHOICES, default=ERIZO)
    producto = models.CharField(max_length=150, choices=PRODUCT_CHOICES, default=ROPA)
    precio = models.CharField(max_length=20)
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)

    def __str__(self):
        return self.animal