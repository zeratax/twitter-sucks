# Standard library imports...
# from collections import namedtuple
import os
import pprint
import sys

# Third-party imports...
import numpy as np
import pandas as pd
import yaml
import tweepy


class Config:
    def __init__(self, data):
        self.data = data
        self.options = None
        self.load()

    def load(self):
        dictionary = None
        if type(self.data) is dict:
            dictionary = self.data
        else:
            try:
                with open(self.data, 'r') as stream:
                    dictionary = yaml.load(stream)
            except IOError as e:
                sys.exit(e)

        # recusively set dictionary to class properties
        for k, v in dictionary.items():
            setattr(self, k, v)
        # self.x = namedtuple('config',
        #                     dictionary.keys())(*dictionary.values())

    def update(self, data):
        self.data = data
        self.options = None
        self.load()


class Twitter:
    def __init__(self, user):
        self.api = self.login()
        self.user = user

    def login(self):
        auth = tweepy.OAuthHandler(config.twitter['consumer_token'],
                                   config.twitter['consumer_secret'])
        auth.set_access_token(config.twitter['access_token'],
                              config.twitter['access_token_secret'])
        return tweepy.API(auth)

    def test(self):
        pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(self.api.get_status(1022072160150540293)._json)
        # print(self.api.get_status(1014243053136171008).favorite_count)
        pp.pprint(self.api.favorites("zeratax"))
        # print(self.api.followers("zeratax", -1))
        # print(self.api.search("from:zeratax"))

    def get_info(self):
        self.followers_count = 
        self.tweets_count =
    
    def get_followers(self):
        return self.api.followers(self.user, -1)

    def get_likes(self, target):
        likes = self.api.favorites(target, -1)
        engagement = []
        for like in likes:
            if like.author == self.user:
                engagement.append(like)

        return engagement

    def get_replies(self, target):
        replies = []
        str = "from:{} to:{}".format(target, self.user)
        i = 0

        while(true):
            i += 1
            search = self.api.search(str, i)
            if search:
                replies.append(search)
            else:
                break
    
    def sucks(self):
        followers = self.get_followers()
        c = ['followers', 'likes', 'replies']
        df = pd.DataFrame(columns=c)
        
        for follower in followers:
            likes = len(get_likes(follower))
            replies = len(get_replies(follower))
            df.append({'followers': follower,
                       'likes': likes,
                       'replies': replies},
                      ignore_index=True) 
        return df
              

if __name__ == '__main__':
    config = Config('config.yaml')
    twitter = Twitter(config.user)
    twitter.test()
