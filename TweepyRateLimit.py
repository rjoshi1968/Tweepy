import tweepy
import json
import re
from re import sub
import time
import codecs
import csv
consumer_key = '41f4jMw17VHTc8ZBsOca7Cd39'
consumer_secret = 'CwzxUBicFLJgplllmePrSwaGY9IWqUSPQOQfD8f1GVI4wSwfJb'

access_token_key = '2938791090-OkfIN7Wm31ZMRspdHVSsDCJordKgPHtmHIB7Dzo'
access_token_secret = 'mrWaQqhllhMDM17JqbBLkTgF9OPAzW7jCJ1bx5iaPmAed'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api = tweepy.API(auth)
print (api.me().name)




RateStatus = api.rate_limit_status()
#decoded = json.loads(RateStatus)
 
    # pretty printing of json-formatted string
for key, value in dict.items(RateStatus['resources']['name']):
    print(key,value)

#print (json.dumps(RateStatus, sort_keys=True, indent=4))
'''
