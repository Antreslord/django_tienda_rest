from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre}, {self.email} han sido creados exitosamente"

class Compra(models.Model):
    TIPO_ENTREGA = [
            ('contraentrega', 'Contraentrega'),
            ('en_oficina', 'En_oficina'),
            ('en_direccion', 'En_direccion')
        ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='compras')
    tipo = models.CharField(max_length=20, choices=TIPO_ENTREGA)
    producto = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{self.cliente.nombre} - {self.producto} - {self.monto}"

