from django.contrib import admin
from .models import Venue, Event
from .forms import VenueAdminForm


class VenueAdmin(admin.ModelAdmin):
    form = VenueAdminForm


admin.site.register(Venue, VenueAdmin)
admin.site.register(Event)
