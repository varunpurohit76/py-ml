# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 22:19:47 2017

@author: Varun
"""

import pandas as pd

# importing and seperating the target
dataset = pd.read_csv('50_Startups.csv')
cols = len(dataset.columns)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, cols-1].values

# encoding values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
x[:, 3] = labelencoder_x.fit_transform(x[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
x = onehotencoder.fit_transform(x).toarray()

# avoiding dummy variable trap
x = x[:, 1:]

# divide into test and train
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# fit
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predict
y_pred = regressor.predict(x_test)