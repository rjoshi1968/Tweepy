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
user = api.get_user("Kishtwar1996")
print(user.id)

print(user.name,"friend Count",user.friends_count,"Location:",user.location)
FriendsIds =[]
FriendsIds = api.friends_ids(id=user.id)
print(FriendsIds)
#timeline = api.user_timeline(screen_name=user.screen_name, include_rts=False, count=100)
#for tweet in timeline:
#    print(str(tweet.id)+ ">>>"+ tweet.text)


#print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
for friend in FriendsIds:
    user = api.get_user(friend)
    timeline = api.user_timeline(screen_name=user.screen_name, include_rts=False, count=100)
    print('User Name: ',user.screen_name)
    
    
    
    
    
