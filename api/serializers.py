from rest_framework import serializers
from .models import Compra, Cliente

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['id', 'cliente', 'producto', 'tipo', 'monto', 'fecha']
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email']

class DetalleCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['producto', 'monto', 'fecha']