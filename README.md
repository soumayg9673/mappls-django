# mappls-map-widget

Mappls Map Widget for Django  
Easily embed Mappls maps and PIN location previews in your Django forms.

## Features

- Django form widget for Mappls PIN with map preview
- Customizable zoom and pitch
- Simple integration with your forms

## Installation

```bash
pip install mappls-map-widget
```

## Usage

Add the widget to your Django form:

```python
from django import forms
from mappls_map_widget.widgets import MapplsPinWithMapEmbedWidget

class LocationForm(forms.Form):
    pin = forms.CharField(widget=MapplsPinWithMapEmbedWidget(zoom=10, pitch=2))
```

## Requirements

- Python 3.7+
- Django 3.2+

## Development

Clone the repo and install dependencies:

```bash
git clone https://github.com/soumayg9673/mappls-django.git
cd mappls-django
pip install -e .
```

## Django Setup

Add `mappls_map_widget` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ... other apps ...
    'mappls_map_widget',
]
```

## License

MIT

## Author

Soumay Gupta  
pmrs9673@gmail.com