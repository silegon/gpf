import sys
import os

sys.path.append('/home/silegon/gpf/github_private_feed')
os.environ['DJANGO_SETTINGS_MODULE'] = 'github_private_feed.settings'

import django
django.setup()

import datetime
import feedparser

FEED_URL = "https://github.com/silegon.private.atom?token=AAmybFO4OaArmKriu87VVo2ls6yEH5mfks66wszowA=="

import json
from bs4 import BeautifulSoup

#from feed.models import GithubUser, Repository, Event
#from feed.cid import FEED_EVENT_QUERY_DICT

def test_parser():
    d = feedparser.parse(FEED_URL)
    print(len(d.entries))
    event_set = set()

    for entry in d.entries:
        #event = entry.id.split(':')[2].split('/')[0]
        #if event in event_set:
        #    continue
        #else:
        #    print(json.dumps(entry, sort_keys=True, indent=4))
        #    event_set.add(event)
        if 'go-travis-test' in entry.link:
            print(json.dumps(entry, sort_keys=True, indent=4))
    #print(len(event_set))
        #username = entry.author_detail["name"]
        #avatar = entry.media_thumbnail[0]['url']
        #print(username, avatar)


def parse_entry_html(entry_html):
    soup = BeautifulSoup(entry_html)
    try:
        repo_desc = soup.find("div",class_="repo-description").p
    except:
        repo_desc = ""

    update_str = soup.find('p','f6').find_all('span')[-1].text
    language = soup.find('p','f6').find('span', itemprop="programmingLanguage")
    event_time_str = soup.find('relative-time')['datetime']
    if language:
        language = language.text
    extra = soup.find('p','f6').find_all('a','muted-link')
    repo_name = soup.find('div','f4').a.text
    len_extra = len(extra)

    star = '0'
    issues = ""
    if len_extra == 2:
        star = extra[0].text
        issues = extra[1].text.split()[0]
    elif len_extra == 1:
        star = extra[0].text
    if '\n' in star:
        star = star.replace('\n','')
    if star.endswith('k'):
        star_count = int(float(star[:-1])*1000)
    else:
        star_count = int(star)

    event_time = datetime.datetime.strptime(event_time_str, "%Y-%m-%dT%H:%M:%SZ")
    repo_update_time = datetime.datetime.strptime("2019 " + update_str[8:], "%Y %b %d")

    return {
        "repo_desc":repo_desc,
        "repo_update_str":update_str,
        "repo_update_time":repo_update_time,
        "event_time_str":event_time_str,
        "event_time":event_time,
        "language":language,
        "repo_name":repo_name,
        "star":star,
        "star_count":star_count,
        "issues":issues,
    }


def parse_feed():
    feed_list = []
    d = feedparser.parse(FEED_URL)
    for entry in d.entries:
        event = entry.id.split(':')[2].split('/')[0]
        event_id = entry.id.split('/')[1]
        username = entry.author_detail["name"]
        avatar = entry.media_thumbnail[0]['url'].split('?')[0]
        user_id = avatar.split('/')[-1]
        entry_dict = {
            "username":username,
            "user_id":user_id,
            "avatar":avatar,
            "event":event,
            "event_id":event_id,
        }
        parse_result_dict = parse_entry_html(entry.summary)
        entry_dict.update(parse_result_dict)
        print(entry_dict)
        feed_list.append(entry_dict)
    return feed_list


def generate_data(feed_list):
    """
    {'username': 'manucorporat', 'user_id': '127379', 'avatar': 'https://avatars3.githubusercontent.com/u/127379', 'event': 'ForkEvent', 'event_id': '8891521610', 'repo_desc': <p>A modular minifier, built on top of the PostCSS ecosystem.</p>, 'repo_update_str': 'Updated Apr 16', 'repo_update_time': datetime.datetime(2019, 4, 16, 0, 0), 'event_time_str': '2019-01-15T17:37:49Z', 'event_time': datetime.datetime(2019, 1, 15, 17, 37, 49), 'language': 'CSS', 'repo_name': 'cssnano/cssnano', 'star': '3k', 'star_count': 3000, 'issues': '7'}
    """
    for feed_item in feed_list:

        user_id = feed_item['user_id']
        github_user, created = GithubUser.objects.get_or_create(user_id=user_id)
        if created:
            github_user.avatar = feed_item['avatar']
            github_user.username = feed_item['username']
            github_user.save()

        repo_name = feed_item['repo_name']
        repository, created = Repository.objects.get_or_create(repo_name=repo_name)
        if created:
            repository.desc = feed_item['repo_desc']
            repository.main_language = feed_item['language']
            repository.star_count = feed_item['star_count']
            repository.issues_count = feed_item['issues']
            repository.update = feed_item['repo_update_time']
            repository.save()

        event, created = Event.objects.get_or_create(event_id=feed_item['event_id'])
        if created:
            event.user = github_user
            event.repository = repository
            event.create = feed_item['event_time']
            event.event_type = FEED_EVENT_QUERY_DICT[feed_item['event']]


if __name__ == "__main__":
    feed_list = parse_feed()
    #generate_data(feed_list)
    #test_parser()
