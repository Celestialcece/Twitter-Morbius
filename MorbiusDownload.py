import tweepy
import requests
from time import sleep
from credentials import *
import os, os.path

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
DIR = "Directory"
imcount = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) - 5
ids = []


while True:
    loopc = 0
    for tweet in api.search_tweets(q="Morbius" or "morbius" or "MoRbIuS" or "mOrBiUs" or "#Morbius" or "#morbius" or "#MoRbIuS" or "#mOrBiUs", include_entities=True, count=100):
        try:
            loopc += 1
            print(loopc)
            print('\nTweet by: @' + tweet.user.screen_name)
            if loopc == 100:
                sleep(900)
            elif tweet.id not in ids:
                if 'media' in tweet.entities:
                    ids.append(tweet.id)
                    print(ids)
                    for image in  tweet.entities['media']:
                        imcount += 1
                        local_filename = "MorbiusImage" + str(imcount) + ".jpg"
                        with requests.get(image['media_url'], stream=True) as r:
                            r.raise_for_status()
                            with open(local_filename, 'wb') as f:
                                for chunk in r.iter_content(chunk_size=8192):
                                    f.write(chunk)
                        f.close()
            else:
                continue
        except tweepy.errors.HTTPException as e:
            print(e)
            sleep(900)
        except StopIteration:
            sleep(900)
