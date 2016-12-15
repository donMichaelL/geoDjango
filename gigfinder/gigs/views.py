from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render_to_response


class LookupView(View):
    def get(self, request):
        return render_to_response('gigs/lookup.html')
