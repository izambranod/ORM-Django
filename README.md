# ORM-Django
Realizar operaciones entre modelos usando el ORM de Django
## Insertar registros en los modelos
Insertar al modelo Producto:
```bash
P= Producto(descripcion='Aceite Girazol',precio=1.50,stock=2000)
P.save()
Producto.objects.create(descripcion='Coca Cola',precio=0.90,stock=10000)
```
Insertar al modelo Cliente:
```bash
C= Cliente(ruc='0959006775001',nombre:'Israel Zambrano',direccion='Milagro')
C.save()
Cliente.objects.create(ruc='0957835555001',nombre:'Daniel Vera',direccion='Guayaquil')
```
Insertar al modelo Factura:
```bash
F= Factura(fecha='2020-07-31',total=16.0,cliente_id=1)
F.save()
Factura.objects.create(fecha='2020-07-21',total=36.25,cliente_id=2)
```
Insertar al modelo DetalleFactura:
```bash
D= DetalleFactura(cantidad=16,precio=1.5,subtotal=1,factura_id=1,producto_id=1)
D.save()
DetalleFactura.objects.create(cantidad=6,precio=2.5,subtotal=15,factura_id=2,producto_id=2)
```
## Actualizar registros en los modelos
Actualizar en el modelo Producto:
```bash
p = Producto.objects.get(id=1) 
p.precio=1.3
p.save()
Producto.objects.filter(id=1).update(precio=1.7)
```
Actualizar en el modelo Cliente:
```bash
c = Cliente.objects.get(id=1)
c.nombre='Moises Zambrano'
c.save()
Cliente.objects.filter(id=2).update(nombre='Yina')
```
Actualizar en el modelo Factura:
```bash
f= Factura.objects.get(id=1)
f.total=15.0
f.save()
Factura.objects.filter(id=2).update(total=25.25,fecha='2020-07-25')
```
Actualizar en el modelo DetalleFactura:
```bash
d= DetalleFactura.objects.get(id=1)
d.cantidad=12
d.save()
DetalleFactura.objects.filter(id=2).update(cantidad=15,precio=3.5)
```
## Eliminar registros en los modelos
```bash
p=Producto.objects.get(id=2)
p.delete()
Producto.objects.filter(id=6).delete()
p.save()
```
No se podra eliminar el producto con id=6, ya que no existe dicho producto.
## Query de un modelo
```bash
1)p=Producto.objects.all()
2)p=Producto.objects.get(id=2)
3)Producto.objects.filter(id__lte=2)
4)Producto.objects.exclude(descripcion__icontains='Cola')
5)Producto.objects.filter(id__gte=4)
6)Producto.objects.filter(id__gt=4).values('id','descripcion')
7)Producto.objects.filter(id__lt=4).values('id','descripcion')
8)Producto.objects.filter(descripcion='Coca Cola').values('id','descripcion')
```
En lo que respecta a la consulta del literal 1 y 2, no existe el id=2 en el producto, ya que anteriormente lo eliminamos. Perso si se pudo consultar si cambiamos por un id existente.
## Querys de varios modelo(relacionados)
```bash
1)Factura.objects.filter(cliente__nombre='Daniel Vera’)
2)c= Cliente.objects.get(nombre='Daniel Vera')
3)c.factura_set.all() 
4)c.factura_set.filter(id=2)
5)Factura.objects.select_related('cliente').filter(cliente__nombre='Daniel Vera’)
6)Cliente.objects.prefetch_related('producto').filter(nombre='Daniel Vera').values('nombre','producto__descripcion')
```
