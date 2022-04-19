import tensorflow as tf
from tensorflow.keras.layers import Layer, Input, Dense
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.optimizers import Adam,SGD


import numpy as np

model = load_model('my_model')


#import ordered feature names from txt as feature_names

# add normalization function for white balance features
# wb index list




  
def make_prediction(x_mat):
    out = model.predict(x_mat)
    return(out)




