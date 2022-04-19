from Machine_Learning.sql_tensorflow import sql2numpy
from Machine_Learning.ann import get_model, train_model

X,Y = sql2numpy()
model = get_model()
train_model(model,X,Y)


