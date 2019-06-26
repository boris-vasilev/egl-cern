from django.db import models
from django.contrib.postgres.fields import ArrayField


class Federation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    accounting_name = models.CharField(max_length=100)


class Pledge(models.Model):
    id = models.AutoField(primary_key=True)
    federation = models.ForeignKey(Federation, on_delete=models.PROTECT)


class Site(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    tier = models.IntegerField()
    supported_vos = ArrayField(models.CharField(max_length=30))
    country = models.CharField(max_length=30)
    country_code = models.CharField(max_length=10)
    federation = models.ForeignKey(Federation, on_delete=models.PROTECT)


class Transfer(models.Model):
    id = models.AutoField(primary_key=True)
    transferred_volume = models.FloatField()
    source = models.OneToOneField(Site, related_name='data_transfer_source', on_delete=models.PROTECT)
    destination = models.OneToOneField(Site, related_name='data_transfer_destination', on_delete= models.PROTECT)
