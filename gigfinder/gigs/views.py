from django.shortcuts import render
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from .models import Event
from .forms import LookupForm

from django.shortcuts import render


class LookupView(FormView):
    form_class = LookupForm
    template_name = 'gigs/lookup.html'
    success_url = reverse_lazy('lookup')

    def form_valid(self, form, **kwargs):
        # Get data
        latitude = form.cleaned_data['latitude']
        longitude = form.cleaned_data['longitude']
        location = Point(longitude, latitude, srid=4326)
        events = Event.objects.annotate(distance=Distance('venue__location', location)).order_by('distance')[0:5]
        return render(self.request, 'gigs/lookupresults.html', {'events': events})
