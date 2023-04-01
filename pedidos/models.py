from djongo import models

class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)
    mesa = models.IntegerField("Nro de mesa")
    listo = models.BooleanField("Listo para servir")
    fecha_pedido = models.DateTimeField("Fecha del pedido", auto_now_add=True)
    lista_productos = models.JSONField("Lista de productos")
    total_precio = models.IntegerField("Precio total")