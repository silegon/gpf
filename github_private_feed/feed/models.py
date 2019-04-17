from django.db import models

from django.contrib.auth.models import User

import feed.cid as FEED_CID


class GithubUser(models.Model):
    username = models.CharField(max_length=64, blank=True, null=True)
    avatar = models.URLField(blank=True, max_length=255, default='')
    uid = models.IntegerField(default=0)
    #nickname = models.CharField(max_length=64, blank=True, null=True)
    #location = models.CharField(max_length=64, blank=True, null=True)
    #intro = models.CharField(blank=True, max_length=255, default='')
    #status_desc = models.CharField(blank=True, max_length=255, default='')


class Repository(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    desc = models.CharField(blank=True, max_length=255, default='')
    main_language = models.CharField(max_length=32)
    star_count = models.IntegerField(default=0)
    issues_count = models.IntegerField(default=0)
    update = models.DateTimeField(blank=True, null=True)


class Event(models.Model):
    user = models.ForeignKey(GithubUser)
    event_type = models.IntegerField(choices=FEED_CID.FEED_EVENT_CHOICES)
    event_id = models.IntegerField(blank=True, null=True)
    repository = models.ForeignKey(Repository)
    create = models.DateTimeField(blank=True, null=True)


class UserStar(models.Model):
    user = models.ForeignKey(GithubUser)
    repository = models.ForeignKey(Repository)
