# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 15:55:32 2017

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


# feature scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)

from sklearn.svm import SVR
svr_regressor = SVR(kernel = "rbf")
svr_regressor.fit(x, y)

y_pred = sc_y.inverse_transform(svr_regressor.predict(sc_x.transform(np.array([[6.5]]))))

plt.scatter(x, y, color = 'red')
plt.plot(x, svr_regressor.predict(x), color = 'blue')
plt.show()