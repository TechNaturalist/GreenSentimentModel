import pandas
import numpy
import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def addSentimentScore(df):
	pass

search_tweets ='searchTweets_recent_2020_04_08.csv'
analyzer = SentimentIntensityAnalyzer()

df = pandas.read_csv(search_tweets)

df = df.drop(df.index[504])

#df['neg'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['neg'])
#df['neu'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['neu'])
#df['pos'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['pos'])
#df['compound'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['compound'])

print(df)
