from rest_framework import serializers
from .models import Pedido
import json

class ProductoCantidadSerializer(serializers.Serializer):
    producto_id = serializers.IntegerField()
    cantidad = serializers.IntegerField()

class PedidoSerializer(serializers.ModelSerializer):
    
    lista_productos = ProductoCantidadSerializer(many=True)
    
    class Meta:
        model = Pedido
        fields = ['id', 'mesa', 'listo', 'fecha_pedido', 'lista_productos', 'total_precio']

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['lista_productos'] = json.loads(representation['lista_productos'])
    #     return representation
    