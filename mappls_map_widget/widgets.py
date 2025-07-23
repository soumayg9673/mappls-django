from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class MapplsPinWithMapEmbedWidget(forms.TextInput):
    def __init__(self, zoom=16, pitch=1, attrs=None):
        super().__init__(attrs)
        self.zoom = zoom
        self.pitch = pitch

    def render(self, name, value, zoom=16, pitch=1, attrs=None, renderer=None):
        final_attrs = self.build_attrs(self.attrs, attrs)
        input_html = super().render(name, value, final_attrs, renderer)

        context = {
            'widget': {
                'name': name,
                'value': value or '',
                'input': input_html,
            },
            'zoom': self.zoom,
            'pitch': self.pitch,
        }
        return mark_safe(render_to_string('mappls_pin_with_embed_widget.html', context))
