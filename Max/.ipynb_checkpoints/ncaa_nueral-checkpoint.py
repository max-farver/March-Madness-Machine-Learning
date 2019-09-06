import pandas as pd
import numpy as numpy

# import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# import os
# os.environ["CUDA_VISIBLE_DEVICES"]="0"

import keras
from keras.models import Sequential, save_model, load_model
from keras.layers import Dense
import tensorflow as tf



from sklearn.model_selection import  cross_val_score, cross_val_predict, train_test_split
from sklearn.metrics import r2_score, accuracy_score

data = pd.read_hdf("processed.h5", key='df')
Y = data['winner']
X = data.drop(columns=['winner', 'TeamID_x','TeamID_y'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42)


classifier = Sequential()

classifier.add(Dense(
    units=12,
    kernel_initializer='uniform',
    activation='relu',
    input_dim=len(X_train.columns)
    ))

classifier.add(Dense(
    units=12,
    kernel_initializer='uniform',
    activation='relu'
    ))

classifier.add(Dense(
    units=12,
    kernel_initializer='uniform',
    activation='relu'
    ))

classifier.add(Dense(
    units=12,
    kernel_initializer='uniform',
    activation='relu'
    ))

classifier.add(Dense(
    units=12,
    kernel_initializer='uniform',
    activation='relu'
    ))

classifier.add(Dense(
    units=1,
    kernel_initializer='uniform',
    activation='sigmoid'
    ))

classifier.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = ['accuracy']
    )

classifier.fit(X_train, y_train, batch_size=256, epochs=1000)

ann_predictions = classifier.predict(X_test)
ann_predictions[ann_predictions > .5] = 1
ann_predictions[ann_predictions <= .5] = 0
ann_accuracy = accuracy_score(y_test, ann_predictions)
print(ann_accuracy)

classifier.save('ncaa_neural.h5')
