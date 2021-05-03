import os
import json
import numpy as np
import pandas as pd
import requests

def auth():
	return os.environ.get("BEARER_TOKEN")


def create_url(tweetId):
	tweet_fields = "tweet.fields=lang,author_id,public_metrics"
	# Tweet fields are adjustable.
	# Options include:
	# attachments, author_id, context_annotations,
	# conversation_id, created_at, entities, geo, id,
	# in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
	# possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
	# source, text, and withheld
	ids = "ids=" + tweetId
	print(ids)
	# You can adjust ids to include a single Tweets.
	# Or you can add to up to 100 comma-separated IDs
	url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
	return url


def create_headers(bearer_token):
	headers = {"Authorization": "Bearer {}".format(bearer_token)}
	return headers


def connect_to_endpoint(url, headers):
	response = requests.request("GET", url, headers=headers)
	print(response.status_code)
	if response.status_code != 200:
		raise Exception(
			"Request returned an error: {} {}".format(
				response.status_code, response.text
		)
	)
	return response.json()


df = pd.read_csv("recent_search_april_04_08_addedscores.csv", index_col=0)

bearer_token = auth()

tweetIds = df['id']
url = create_url(str(tweetIds[0]))
headers = create_headers(bearer_token)
json_response = connect_to_endpoint(url,headers)

json_response['data']['0']['author_id']
json_response['data']['0']['public medtrics']['retweet_count']
json_response['data']['0']['public medtrics']['reply_count']
json_response['data']['0']['public medtrics']['like_count']
json_response['data']['0']['public medtrics']['quote_count']
