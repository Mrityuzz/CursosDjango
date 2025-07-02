# cursos/admin.py
from django.contrib import admin
from .models import Curso, Actividad

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre', 'nivel', 'categoria', 'publicado', 'fecha_creacion')
    list_filter = ('publicado', 'categoria', 'nivel')
    search_fields = ('nombre', 'descripcion', 'clave')
    date_hierarchy = 'fecha_creacion'
    ordering = ['fecha_creacion']
    fieldsets = (
        ("Información general", {
            'fields': ('clave', 'nombre', 'descripcion', 'nivel', 'categoria', 'publicado')
        }),
        ("Multimedia y metadatos", {
            'fields': ('portada', 'fecha_creacion'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('fecha_creacion',)

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ("clave", "curso", "fecha_creacion")
    search_fields = ("clave", "curso__nombre")
    list_filter = ("curso",)
    date_hierarchy = "fecha_creacion"
    readonly_fields = ("fecha_creacion",)
    fieldsets = (
        ("Información de la Actividad", {
            "fields": ("curso", "clave", "descripcion")
        }),
        ("Datos automáticos", {
            "fields": ("fecha_creacion",)
        }),
    )


    