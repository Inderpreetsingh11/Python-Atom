import tweepy
import json

id_of_liked_tweets = []
id_of_retweeted_tweets = []

def Authentication(API_KEY,API_SECRET,ACCESS_KEY,ACCESS_SECRET):
    auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
    auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def get_like_ids(api):
    for tweet in api.favorites(screen_name = 'Inder4632'):
        id_of_liked_tweets.append(tweet.id)
    return id_of_liked_tweets

def retweet_liked_tweets(id,api):
    try:
        api.retweet(id)
    except tweepy.TweepError as e:
        print(e)

def get_retweets_home_timeline(api):
    for tweet in api.home_timeline():
        if tweet.retweet_count != 0:
            id_of_retweeted_tweets.append(tweet.retweeted_status.id)
    return id_of_retweeted_tweets
