import tweepy
import os
import services as twitter
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_KEY = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

api = twitter.Authentication(API_KEY,API_SECRET,ACCESS_KEY,ACCESS_SECRET)

for id in twitter.get_like_ids('Inder4632',api):
    twitter.retweet_liked_tweets(id,api)
