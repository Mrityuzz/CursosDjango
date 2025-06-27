# cursos/models.py
from django.db import models

class Curso(models.Model):
    clave = models.CharField("Clave del curso", max_length=10, unique=True)
    nombre = models.CharField("Nombre del curso", max_length=100)
    descripcion = models.TextField("Descripción")
    nivel = models.IntegerField("Nivel de dificultad")
    publicado = models.BooleanField("¿Publicado?")
    categoria = models.CharField("Categoría", max_length=50, choices=[
        ('web', 'Web'),
        ('data', 'Datos'),
        ('ai', 'Inteligencia Artificial'),
        ('seg', 'Ciberseguridad'),
    ])
    portada = models.ImageField("Imagen de portada", upload_to='cursos/')
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['fecha_creacion']
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
