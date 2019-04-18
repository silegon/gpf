import json
import datetime
from django.shortcuts import render
from feed.models import Event

def private_feed(request):
    events = Event.objects.all()[:1]
    context = {
        "events":events,
    }
    return render(request, 'feed/private_feed.html', context, content_type='application/xml')
    #return render(request, 'feed/private_feed.html', context, content_type='application/atom+xml')

def tpf(request):
    context = {}
    return render(request, 'feed/dev_private_feed.html', context, content_type='xml')
