from django.db import models

# Create your models here.
class Edificio(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30, unique=True)
    tipo_edificio = (
        ('recidencial', 'Recidencial'),
        ('comercial', 'Comercial'),
        )
    tipo = models.CharField(max_length=100,choices=tipo_edificio)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

    def obtener_costo_departamentos(self):
        # valor = [t.costo_plan for t in self.numeros_telefonicos.all()]
        # valor = sum(valor)  # [10.2, 20]
        valor = 0;
        for t in self.departamentos.all(): # self.num_telefonicos -> me devuelve un listado de obj de tipo NumeroTelefonico
            valor = valor + t.costo
        return valor

    def obtener_cantidad_cuartos(self):
        """
        """
        valor = 0
        for t in self.departamentos.all():
            valor += t.numero_cuartos
        return valor


class Departamento(models.Model):
    nombrePropietario = models.CharField(max_length=100)
    costo = models.FloatField(max_length=100)
    numero_cuartos = models.IntegerField(max_length=100)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %f %d" % (self.nombreDep, self.costo, self.numero_cuartos)