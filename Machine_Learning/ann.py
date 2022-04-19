from tensorflow.keras.layers import Layer, Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam,SGD
from sklearn.model_selection import train_test_split

def get_model():
    i = Input(5)
    x = Dense(20, activation='relu')(i)
    x = Dense(20, activation='relu')(x)
    x = Dense(20, activation='relu')(x)
    x = Dense(20, activation='relu')(x)
    x = Dense(3)(x)

    model = Model(i,x)
    model.compile(loss='mse', optimizer='adam')
    return model
    
def train_model(model,X,Y):
    X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=.2, random_state=42)
    model.fit(X_train,y_train, validation_data=(X_test,y_test), epochs = 40, batch_size=1024)
    model.save('WB_model')

