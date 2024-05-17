from django.contrib import admin

# Register your models here.
from TiendaVirtual.models import CarritoCompra, Categoria, Color, MetodoPago, Pedido, Producto, Talla

admin.site.register(CarritoCompra)
admin.site.register(Categoria)
admin.site.register(Color)
admin.site.register(MetodoPago)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Talla)