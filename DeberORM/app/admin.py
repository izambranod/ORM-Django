from .models import Producto, Cliente, Factura, DetalleFactura
from django.contrib import admin

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
