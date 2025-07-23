from django import forms

from .models import Place
from mappls_map_widget.widgets import MapplsPinWithMapEmbedWidget

class PlaceForm(forms.Form):
    class Meta:
        model = Place
        fields = ['name', 'mappls_pin']
        widgets = {
            'mappls_pin': MapplsPinWithMapEmbedWidget(
                zoom=16,
                pitch=1,
            ),
        }
        labels = {
            'name': 'Place Name',
            'mappls_pin': 'Mappls Pin',
        }