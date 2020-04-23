import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = "ewZHMriAM7nVqiat2N3y9PwQ3"
credentials['CONSUMER_SECRET'] = "Njj8vkUKLtSXpwavMyRsYWpLUQchjRzjOXY8FoXIFz0ff6bW4h"
credentials['ACCESS_TOKEN'] = "1219180125767524352-3U1rsK4b75ricKToClxUXjnT5sqRex"
credentials['ACCESS_SECRET'] = "33ilPHqr8KEdo2GKFs4ChOKNVDpqZTkNOFnovdVrjnQhK"

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)