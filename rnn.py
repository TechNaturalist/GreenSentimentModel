import pandas as pd
import tensorflow as tf
import numpy as np

from keras.models import Sequential
from keras.layers import Dense

df = pd.read_csv("all_tweets_tweet_dataadded.csv", index_col=0)

data_array = df.to_numpy()


#Getting Inputs

true_input  = np.asarray(data_array[:,2:6])

#Get Output

true_output = np.asarray(data_array[:,6:10])

iput = tf.constant(true_input, dtype=tf.float64)
ouput = tf.constant(true_output,dtype=tf.float64)

model = Sequential()
model.add(Dense(10, input_dim = 4, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(4, activation='relu'))

model.compile(loss='mae', optimizer='adam', metrics=[tf.keras.metrics.MeanSquaredError()])

model.fit(iput, ouput, epochs = 1000000, batch_size = 200);

_, accuracy = model.evaluate(iput, ouput);

#print('Accuracy: %.2f' %(accuracy*100))

model.save('model_newst.h5')

model.save_weights('model_weights.h5')
