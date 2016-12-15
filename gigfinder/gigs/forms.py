from django.conf import settings
from django.forms import ModelForm, Form, FloatField
from floppyforms.gis import PointWidget, BaseGMapWidget, PolygonWidget
from .models import Venue, Area


class CustomPointWidget(PointWidget, BaseGMapWidget):
    google_maps_api_key = settings.GOOGLE_MAP_API_KEY
    class Media:
        js = ('/static/floppyforms/js/MapWidget.js',)


class VenueAdminForm(ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'location']
        widgets = {
            'location': CustomPointWidget()
        }


class CustomAreaWidget(PolygonWidget, BaseGMapWidget):
    google_maps_api_key = settings.GOOGLE_MAP_API_KEY
    class Media:
        js = ('/static/floppyforms/js/MapWidget.js',)


class AreaAdminForm(ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'area']
        widgets = {
            'area': CustomAreaWidget()
        }


class LookupForm(Form):
    latitude = FloatField()
    longitude = FloatField()
