# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:59:10 2017

@author: Varun
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importing and seperating the target
dataset = pd.read_csv('Position_Salaries.csv')
cols = len(dataset.columns)
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, cols-1].values

# model
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 42)
regressor.fit(x, y)

# predict
y_pred = regressor.predict(6.5)

# plot
x_grid = np.arange(min(x), max(x), 0.01)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'blue')
plt.plot(x_grid, regressor.predict(x_grid), color = 'red')
plt.show()