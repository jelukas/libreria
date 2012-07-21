from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField(blank=True)
    categoria = models.ForeignKey('Categoria', related_name='libros')

    def __str__(self):
        return self.titulo


class Autor(models.Model):
    nombre = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    libros = models.ManyToManyField('Libro', related_name='autores')

    def __str__(self):
        return self.nombre + " " +  self.apellidos


class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
