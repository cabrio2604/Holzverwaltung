from django.contrib import admin
from .models import Lieferant, Lieferung, Artikel, Lieferposition, Lagerplatz

# Register your models here.

admin.site.register(Lieferant)
admin.site.register(Lieferung)
# admin.site.register(Artikel)
admin.site.register(Lieferposition)
# admin.site.register(Lagerplatz)

# SHIFT + ALT + PFEIL_DOWN


@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    search_fields = ['bezeichnung', 'bemerkung']
    list_display = ['bezeichnung', 'liefereinheit', 'ekpreis']

@admin.register(Lagerplatz)
class LagerplatzAdmin(admin.ModelAdmin):
    list_filter = ['artikel']