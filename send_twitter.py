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


# Post a tweet from Python
api.update_status("Look, I'm tweeting from #Python! www.fiverr.com/coderjs")
# Your tweet has been posted!