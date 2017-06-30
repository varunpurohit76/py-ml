# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 22:56:19 2017

@author: Varun
"""

import pandas as pd
import matplotlib.pyplot as plt

# importing and seperating the target
dataset = pd.read_csv('Position_Salaries.csv')
cols = len(dataset.columns)
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, cols-1].values

# fit to linear model
from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(x, y)

# plot linear regression
plt.scatter(x, y, color = 'red')
plt.plot(x, linear_regressor.predict(x), color = 'blue')
plt.show()

# fit to polynomial regression
from sklearn.preprocessing import PolynomialFeatures
polynomial_regressor = PolynomialFeatures(degree = 3)
x_poly = polynomial_regressor.fit_transform(x)
linear_regressor_polynomial = LinearRegression()
linear_regressor_polynomial.fit(x_poly, y)


#plot polynomial regression
plt.scatter(x, y, color = 'red')
plt.plot(x, linear_regressor_polynomial.predict(polynomial_regressor.fit_transform(x)), color = 'blue')
plt.show()