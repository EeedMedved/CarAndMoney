from django.db import models


class Refill(models.Model):
    refillDate = models.DateField()
    mileage = models.IntegerField(unique=True)
    liters = models.SmallIntegerField()
    gas_station = models.ForeignKey('GasStation', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    comment = models.CharField(max_length=100, blank=True, null=True)

    @property
    def sum(self):
        return self.liters * self.price

    def __str__(self):
        return self.gas_station.name + ' ' + str(self.refillDate)


class GasStation(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    class Meta:
        unique_together = ['name', 'location']

    def __str__(self):
        return self.name + ', ' + self.location