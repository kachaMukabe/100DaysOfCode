import sys
sys.path.append('../')

from time import sleep
from D2_tweet_blog_stories.read_blog import *
from D2_tweet_blog_stories.credentials import *
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def tweet():
    for line in get_post_links():
        try:
            api.update_status(line)
            sleep(86400)
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)


tweet()
