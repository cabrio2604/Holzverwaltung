from django.contrib import admin
from .models import Lieferant, Lieferung

# Register your models here.

admin.site.register(Lieferant)
admin.site.register(Lieferung)