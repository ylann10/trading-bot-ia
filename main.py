#!/usr/bin/python3

from os.path import exists
from stats import getStats
from pprint import pprint
from environment import *
from time import sleep
from os import system
from sys import exit
from keras import *
import numpy as np

MODEL = 'model.keras'
DATA_LIMIT = 3650

model = Sequential()
model.add(layers.Dense(units=1, input_shape=(6,)))
model.add(layers.Dense(units=256))
model.add(layers.Dense(units=256))
model.add(layers.Dense(units=256))
model.add(layers.Dense(units=1))

if exists(MODEL):
    model = models.load_model(MODEL)
else:
    stats = getStats(DATA_LIMIT)
    entree = np.array(stats['x'], dtype=float)
    sortie = np.array(stats['y'], dtype=float)
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x=entree, y=sortie, epochs=10000)
    model.save(MODEL)

x = np.array(getStats(1, True), dtype=float)
r = model.predict(x, verbose=None)[0][0]
print('Open: ' + str(x[0][0]))
print('High: ' + str(x[0][1]))
print('Low: ' + str(x[0][2]))
print('Close: ' + str(x[0][3]))
print('Volume: ' + str(x[0][4]))
print('Trades: ' + str(x[0][5]))
print('Next close (predicted): ' + str(r))