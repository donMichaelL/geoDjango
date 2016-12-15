from django.contrib import admin
from .models import Venue, Area, Event
from .forms import VenueAdminForm, AreaAdminForm


class VenueAdmin(admin.ModelAdmin):
    form = VenueAdminForm


class AreaAdmin(admin.ModelAdmin):
    form = AreaAdminForm
    



admin.site.register(Venue, VenueAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Event)
