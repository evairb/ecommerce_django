from django.contrib import admin
from pedido import models
# Register your models here.

class ItemPedidoInLine(admin.TabularInline):
    model = models.ItemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInLine
    ]

    
admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.ItemPedido)