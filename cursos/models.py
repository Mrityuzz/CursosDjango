from django.db import models

class Curso(models.Model):
    clave = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    publicado = models.BooleanField(default=False)
    portada = models.ImageField(upload_to='cursos/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    clave = models.CharField(max_length=20)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.clave} - {self.curso.nombre}"
