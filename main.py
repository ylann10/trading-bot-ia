#!/usr/bin/python3

from environment import *
from os.path import exists
from stats import getStats
from sys import exit
from keras import *
import numpy as np

MODEL = 'model.keras'
DATA_LIMIT = 3650
MAX_EPOCHS = None
MAX_LOSS = 0.01

model = Sequential()
model.add(layers.Dense(units=1, input_shape=(6,)))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=1))

if exists(MODEL):
    model = models.load_model(MODEL)
else:
    counter = 0
    backup = None
    lastest, min_loss = None, None
    stats = getStats(DATA_LIMIT)
    entree = np.array(stats['x'], dtype=float)
    sortie = np.array(stats['y'], dtype=float)
    model.compile(optimizer='adam', loss='mean_squared_error')
    while True:
        try:
            history = model.fit(x=entree, y=sortie, epochs=1, verbose=0)
            counter += 1
            if not min_loss or history.history['loss'][0] < min_loss:
                min_loss = history.history['loss'][0]
                latest = counter
                backup = model
            if counter % 10 == 0:
                logs = f"Epochs: {counter};"
                logs += f" Min: {min_loss};"
                logs += f" Latest: {counter - latest};"
                logs += f" Cur: {history.history['loss'][0]};"
                print(logs)
            if history.history['loss'][0] <= MAX_LOSS or (MAX_EPOCHS and counter >= MAX_EPOCHS):
                break
        except KeyboardInterrupt:
            if backup:
                model = backup
            model.save(MODEL)
            exit(0)
    model.save(MODEL)

x = np.array(getStats(1, True), dtype=float)
r = model.predict(x, verbose=None)[0][0]
print('Next close (predicted): ' + str(r))