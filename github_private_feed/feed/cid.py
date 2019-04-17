FEED_EVENT_CREATE = 0
FEED_EVENT_WATCH = 1
FEED_EVENT_FORK = 2
FEED_EVENT_PUBLIC = 3

FEED_EVENT_CHOICES = (
    (FEED_EVENT_CREATE, "CreateEvent"),
    (FEED_EVENT_WATCH, "WatchEvent"),
    (FEED_EVENT_FORK, "ForkEvent"),
    (FEED_EVENT_PUBLIC, "PublicEvent")
)

FEED_EVENT_QUERY_DICT = {
    "CreateEvent":FEED_EVENT_CREATE,
    "WatchEvent":FEED_EVENT_WATCH,
    "ForkEvent":FEED_EVENT_FORK,
    "PublicEvent":FEED_EVENT_PUBLIC
}