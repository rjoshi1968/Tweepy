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
user = api.get_user("Kishtwar1996")
print(user.id)

print(user.name,"friend Count",user.friends_count,"Location:",user.location)
query = "pune AND murder"
for tweets in tweepy.Cursor(api.search,q=query, lang="en", count=100).items():
    EncodedTweet = tweets.text.encode("utf-8",errors='ignore')
    print(tweets.author.name,"(",tweets.author.followers_count,
          ")", ">>>",EncodedTweet)

    csvfile = open("MyTweeps.csv",'a')
    csvwriter = csv.writer(csvfile)
    lines = tweets.author.name + ","+ str(tweets.author.followers_count )
    
    csvfile.write(tweets.user.name)
    csvfile.write(',')
    csvfile.write(str(tweets.user.id))
    csvfile.write(',')
    csvfile.write(str(tweets.author.followers_count))
    csvfile.write(',')
    csvfile.write(tweets.text)
    csvfile.write('\n')
    csvfile.close()
    
