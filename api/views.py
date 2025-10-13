from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import response
from rest_framework import status
from .models import Cliente
from .serializers import CompraSerializer, ClienteSerializer, DetalleCompraSerializer
from django.db.models import Sum

# Create your views here.

# @api_view(['GET', 'POST'])
@api_view(['POST'])
def crear_compra(request):

    serializer = CompraSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def crear_cliente(request):
    serializer = ClienteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def compras_por_cliente(request, cliente_id):
    
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        return response.Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)


    compras = cliente.compras.all()
    compras_serializer = DetalleCompraSerializer(compras, many=True)

    data = {
        "cliente": {
            "nombre": cliente.nombre,
            "email": cliente.email
        },
        "compras": compras_serializer.data
    }

    return response.Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def gasto_total_por_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except:
        return response.Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    suma_total = cliente.compras.aggregate(suma_total=Sum('monto'))['suma_total'] or 0

    data = {
        "cliente":{
            "nombre": cliente.nombre,
            "email": cliente.email
        },
        "gasto_total": suma_total
    }

    return response.Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def gastos_por_tipo_entrega(request, cliente_id):

    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        return response.Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    compras = cliente.compras.all()

    resultado = []

    for compra in compras:
        costo = float(compra.monto)

        if compra.tipo == 'contraentrega':
            costo -= 400
        elif compra.tipo == 'en_direccion':
            costo += 400
        elif compra.tipo == 'en_oficina':
            costo = costo
        
        resultado.append({
            "producto": compra.producto,
            "tipo": compra.tipo,
            "monto_original": float(compra.monto),
            "monto_final": costo,
            "fecha": compra.fecha
        })

    data = {
        "cliente": {
            "nombre": cliente.nombre,
            "email": cliente.email
        },
        "compras_por_tipo_entrega": resultado
    }

    return response.Response(data, status=status.HTTP_200_OK)