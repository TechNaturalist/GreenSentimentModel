import nltk
import pandas as pd

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import twitter_samples

nltk.download('twitter_samples')
nltk.download('vader_lexicon')

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

analyzer = SentimentIntensityAnalyzer()

my_labels = [1] * len(all_positive_tweets)
negative_labels = [0] * len(all_negative_tweets)
my_labels.extend(negative_labels)

all_positive_tweets.extend(all_negative_tweets);

##Testing
df = pd.DataFrame({'tweets': all_positive_tweets,
    'my_labels': my_labels})

df['neg'] = df['tweets'].apply(lambda x:analyzer.polarity_scores(x)['neg'])
df['neu'] = df['tweets'].apply(lambda x:analyzer.polarity_scores(x)['neu'])
df['pos'] = df['tweets'].apply(lambda x:analyzer.polarity_scores(x)['pos'])
df['compound'] = df['tweets'].apply(lambda x:analyzer.polarity_scores(x)['compound'])


df.to_csv('all_tweets.csv')



