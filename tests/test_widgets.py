import unittest
from django import forms
from mappls_map_widget.widgets import MapplsPinWithMapEmbedWidget

class DummyForm(forms.Form):
    pin = forms.CharField(widget=MapplsPinWithMapEmbedWidget(zoom=10, pitch=2))

class MapplsPinWithMapEmbedWidgetTest(unittest.TestCase):
    def test_widget_render_with_value(self):
        form = DummyForm(initial={'pin': 'KZ8LQB'})
        html = form.as_p()
        self.assertIn('iframe', html)
        self.assertIn('KZ8LQB', html)
        self.assertIn('zoom=10', html)
        self.assertIn('pitch=2', html)

    def test_widget_render_without_value(self):
        form = DummyForm()
        html = form.as_p()
        self.assertIn('Enter Mappls PIN to preview the location', html)
        self.assertIn('iframe', html)

    def test_widget_attrs(self):
        widget = MapplsPinWithMapEmbedWidget(zoom=5, pitch=3, attrs={'class': 'custom'})
        html = widget.render('pin', 'KZ8LQB')
        self.assertIn('class="custom"', html)
        self.assertIn('KZ8LQB', html)
        self.assertIn('zoom=5', html)
        self.assertIn('pitch=3', html)

if __name__ == "__main__":
    unittest.main()