import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config ['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Add Artist username
screen_name = '_blackDan6'

# Prints the users tweets and data about the tweet
tweets = api.user_timeline(id=screen_name, count=2)

# Selects the first tweet from above response & Show as a JSON
tweet = tweets[1]
tweet._json

# Show attributes of the JSON that you can select.
list(tweet._json.keys())

# Gets the user information & Displays as a JSON
userdata = tweet.user

twitter_username = userdata.screen_name

twitter_id = userdata.id

artist = {
    "username": twitter_username, 
    "twitter_id": twitter_id
}

tweet = {
    "tweet_id": tweet.id,
    "tweet": tweet.text,
    "created_at": tweet.created_at,
    "twitter_id": twitter_id    
}

columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in artist.keys())
values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in artist.values())
sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('artistsTable', columns, values)
print(sql)

columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in tweet.keys())
values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in tweet.values())
sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('tweetsTable', columns, values)
print(sql)



