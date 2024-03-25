from django.contrib import admin
from .models import Dream


# Register your models here.
@admin.register(Dream)
class DreamAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'descriere', 'eticheta', 'stres', 'nivelEnergie', 'durata', 'data', 'created', 'updated']

