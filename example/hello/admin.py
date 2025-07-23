from django.contrib import admin

from .models import Place
from .forms import PlaceForm

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    form = PlaceForm
    list_display = ('name', 'mappls_pin')
    search_fields = ('name', 'mappls_pin')
    ordering = ('name',)
