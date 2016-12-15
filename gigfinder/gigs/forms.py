from django.conf import settings
from django.forms import ModelForm, Form, FloatField
from floppyforms.gis import PointWidget, BaseGMapWidget
from .models import Venue


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


class LookupForm(Form):
    latitude = FloatField()
    longitude = FloatField()
