# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 00:09:09 2019

@author: hrajr
"""

import  matplotlib.pyplot  as plt
X=[1, 1.2, 1.23, 1.3, 1.45, 1.59, 1.75, 1.95, 2.5, 3, 3.5, 5.1, 5.8, 6.6, 7, 7.5, 8.1, 10, 15, 20, 30, 40, 50]
y=[6, 7, 10, 11, 15, 20, 25, 25.5, 26, 26.5, 27, 29, 30, 30.6, 30.9, 31.3, 32.5, 33, 33, 33, 33.3, 32.3, 33.5]
plt.plot(X, y, color = 'blue')
plt.show()
X=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y=[200, 100, 70, 60, 50, 45, 40, 30, 35, 15]
dx=[y[i]-y[i-1] for i in range(1,len(y))]
dy=[y[i]-y[i-1] for i in range(1,len(y))]
plt.plot(X, y, color = 'red')

plt.show()