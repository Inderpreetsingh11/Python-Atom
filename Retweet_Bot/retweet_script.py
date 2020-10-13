import tweepy
import os
import json
import os.path
import services as twitter
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_KEY = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

api = twitter.Authentication(API_KEY,API_SECRET,ACCESS_KEY,ACCESS_SECRET)

likes_list = twitter.get_like_ids(api)

if os.path.exists("liked_tweets_id.json") == False:
    twitter.write_to_json(likes_list)
    for id in likes_list:
        twitter.retweet_liked_tweets(id,api)
else:
    f = open('liked_tweets_id.json',)
    data = json.load(f)
    for id in likes_list:
        if id in data:
            pass
        else:
            twitter.retweet_liked_tweets(id,api)

    f.close()
    with open('liked_tweets_id.json', 'w') as json_file:
        json_file.seek(0)
        json_file.truncate()
        json.dump(likes_list, json_file)
