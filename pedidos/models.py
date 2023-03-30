from djongo import models

class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)
    mesa=models.IntegerField()
    lista_productos = models.JSONField()