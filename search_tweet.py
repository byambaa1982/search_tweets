import os
import tweepy as tw
import pandas as pd
import json

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
	creds = json.load(file)

auth = tw.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tw.API(auth, wait_on_rate_limit=True)


# Define the search term and the date_since date as variables
search_words = "#snowflake"
date_since = "2020-01-16"


# Collect tweets
tweets = tw.Cursor(api.search,
		q=search_words,
		lang="en",
		since=date_since).items(5)

tweets

# Iterate and print tweets
for tweet in tweets:
	print(tweet.text)