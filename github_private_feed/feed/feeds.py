from django.contrib.syndication.views import Feed
from django.urls import reverse
#from policebeat.models import NewsItem
from feed.models import Event

class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        #return Event.objects.order_by('-create')[:5]
        return Event.objects.all()

    def item_title(self, item):
        #return item.title
        return "test title"

    def item_description(self, item):
        #return item.repository.desc
        return ''

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return 'no-link'
