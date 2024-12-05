from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto


class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('id',)


class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    list_display_links = ('nombre',)
    ordering = ('id',)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion',
                    'p_costo', 'p_venta')
    list_display_links = ('nombre',)
    list_filter = ('laboratorio', 'f_fabricacion')
    ordering = ('id',)


admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
