from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, db_index=True)


class Dream(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=255, db_index=True)
    descriere = models.TextField(blank=True)
    eticheta = models.CharField(max_length=255, db_index=True)
    stres = models.DecimalField(max_digits=3, decimal_places=0)
    nivelEnergie = models.DecimalField(max_digits=1, decimal_places=0)
    durata = models.DecimalField(max_digits=1, decimal_places=0)
    data = models.DateTimeField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
