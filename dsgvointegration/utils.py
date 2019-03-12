# -*- coding: utf-8 -*-

import tweepy
import time
import json

# Make your settings
consumer_key = 'XXXXX'
consumer_secret = 'XXXXXX'
access_token = 'XXXXXX'
access_token_secret = 'XXXXXX'


entry_examples = [
    {
    'id_str': '22222222',
    'text': 'Tweet Text 1',
    'screen_name': 'eteachingorg',
    'name': 'e-teaching.org',},
    {
    'id_str': '11111111',
    'text': 'Tweet Text 2',
    'screen_name': 'eteachingorg',
    'name': 'e-teaching.org',}            
]


class TwitterTimelineMixin(object):
    """Twitter mixin class """

    def get_tweepy_api(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return tweepy.API(auth)

    def twitter_timeline(self):
        tapi = self.get_tweepy_api()
        timeline = list()
        public_tweets = tapi.home_timeline(count=3, tweet_mode='extended')
        for tweet in public_tweets:
            entry = {
                'id_str': tweet.id_str,
                'text': tweet.full_text,
                'screen_name': tweet.user.screen_name,
                'name': tweet.user.name,}
            timeline.append(entry)
        return timeline

    def timeline_json(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        timeline = json.dumps(entry_examples)
        # Make your settings above and uncomment the following line. 
        # timeline = json.dumps(self.twitter_timeline())
        self.wfile.write(timeline)
        return  
