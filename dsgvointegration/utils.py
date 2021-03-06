# -*- coding: utf-8 -*-

import sys
import tweepy
import json
from dsgvointegration.config import (CONSUMER_KEY, CONSUMER_SECRET,
                                     ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
                                     TWITTER_EXAMPLE, REAL_TIMELINE)


class TwitterTimelineMixin(object):
    """Twitter mixin class """

    def get_tweepy_api(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
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
                'name': tweet.user.name}
            timeline.append(entry)
        return timeline

    def timeline_json(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        if REAL_TIMELINE:
            timeline = json.dumps(self.twitter_timeline())
        else:
            timeline = json.dumps(TWITTER_EXAMPLE)

        if sys.version_info < (3, 0):
            timeline = bytes(timeline)
        else:
            timeline = bytes(timeline, 'utf8')
        self.wfile.write(timeline)

        return
