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

csvFile = open('SearchData2.csv', 'w')
#Use csv Writer
csvWriter = csv.writer(csvFile)

tweets = tweepy.Cursor(api.search,
                           q="#MyJihad",
                                                    
                           include_entities=True,
                           lang="en", count=100).items()
for tweet in tweets:
    csvWriter.writerow([tweet.user.name.encode('utf-8','ignore'),tweet.created_at, tweet.text.encode('utf-8')])
    csvFile.flush()

csvFile.close()


'''


print(tweet.user.name.encode('utf-8','ignore'), tweet.created_at, tweet.text.encode('utf-8','ignore'))

print tweet.created_at, tweet.text
    print(s.author.screen_name.encode(encoding='utf-8',errors='ignore') +
          "(" + s.author.name.encode(encoding='utf-8',errors='ignore') + ") >> "+ s.text.encode(encoding='utf-8',errors='ignore'))

for s in results:
    print(s.text.encode('utf-8'))


#print(api.rate_limit_status())
'''
