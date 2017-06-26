# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:40:39 2017

@author: Varun
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing and seperating the target
dataset = pd.read_csv('Salary_Data.csv')
cols = len(dataset.columns)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, cols-1].values

# divide into test and train
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 42)

# fitting simple linear regression to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predict
y_pred = regressor.predict(x_test)

# visulaization
plt.scatter(x_train, y_train, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary v/s Exp (Train)')
plt.xlabel('Exp')
plt.ylabel('Salary')
plt.show()

plt.scatter(x_test, y_test, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary v/s Exp (Test)')
plt.xlabel('Exp')
plt.ylabel('Salary')
plt.show()