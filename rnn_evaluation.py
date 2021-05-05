import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("all_tweets_tweet_dataadded.csv", index_col=0)
data_array = df.to_numpy()

inputs = np.asarray(data_array[:,2:6])
tf_inputs = tf.constant(inputs, dtype=tf.float64)

outputs = np.asarray(data_array[:,6:10])
tf_outputs = tf.constant(outputs,dtype=tf.float64)


model = tf.keras.models.load_model('model_newst_training.h5')
model.load_weights('model_weights_trianing.h5')

predicted_output = model.predict(tf_inputs)


fig,axs = plt.subplots(2,2)
fig.suptitle("Model Results")

axs[0,0].scatter(predicted_output[:,0],tf_outputs[:,0])
axs[0,1].scatter(predicted_output[:,1],tf_outputs[:,1])
axs[1,0].scatter(predicted_output[:,2],tf_outputs[:,2])
axs[1,1].scatter(predicted_output[:,3],tf_outputs[:,3])

plt.show()
