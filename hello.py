import tweepy
import json

# Load credentials from json file
with open("auth.json", "r") as file:
    creds = json.load(file)


auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)