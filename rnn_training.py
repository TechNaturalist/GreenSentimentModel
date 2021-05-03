import pandas as pd
import tensorflow as tf
import numpy as np


# data
df = pd.read_csv("all_tweets_tweet_dataadded.csv", index_col=0)
data_array = df.to_numpy()

#get inputs and outputs
inputs  = np.asarray(data_array[:,2:6])
outputs = np.asarray(data_array[:,6:10])

train_inputs = tf.constant(inputs, dtype=tf.float64)
train_outputs = tf.constant(outputs,dtype=tf.float64)


#load model
model = tf.keras.models.load_model('model_newst.h5')

model.load_weights('model_weights.h5')

model.fit(train_inputs, train_outputs, epochs = 1000, batch_size = 200);

_, accuracy = model.evaluate(train_inputs, train_outputs);

print('Accuracy: %.2f' %(accuracy*100))

model.save('model_newst_training.h5')

model.save_weights('model_weights_trianing.h5')


