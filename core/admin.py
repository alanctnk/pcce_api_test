from django.contrib import admin

from .models import ObjetoTipo, Objeto, Calibre, Arma, Municao


@admin.register(ObjetoTipo)
class ObjetoTipoAdmin(admin.ModelAdmin):
    list_display = ('tipo_de_objeto',)


@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'calibre_id', 'quantidade_de_tiros', 'valor_estimado', 'imagem')


@admin.register(Municao)
class MunicaoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'calibre_id', 'valor-estimado')

@admin.register(Calibre)
class CalibreAdmin(admin.ModelAdmin):
    list_display = ('desc_calibre', )