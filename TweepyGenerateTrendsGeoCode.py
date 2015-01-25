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
GeoFile = open('GeoFile.csv','at', encoding='utf-8')

TrendsAvailable = api.trends_available()
for item in TrendsAvailable:
    TextToWrite = []
    TextToWrite.append(item['country'])
    TextToWrite.append(item['woeid'])
    TextToWrite.append(item['name'])
    GeoFile.write(str(TextToWrite))
    GeoFile.write('\n')
#    GeoFile.write('-'.join(str(line) for line in TextToWrite))
    
    
GeoFile.close()
    


'''
TextToWrite.append(item['country'].encode("utf-8",errors='ignore'))
    TextToWrite.append(str(item['woeid']).encode("utf-8",errors='ignore'))
    TextToWrite.append(item['name'].encode("utf-8",errors='ignore'))
TrendsByLocation = api.trends_place(2295412)
print(len(str(TrendsByLocation)))
SplitTrends = TrendsByLocation[0]
Trends = SplitTrends['trends']
for trend in Trends:
    print(trend['name'])
'''
