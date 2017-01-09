#!/usr/bin/env python # chebyshev.py

#Chebyshev polynomial
import numpy as np
import matplotlib.pyplot as plt

slices = 100
lower = -1.
upper = 1.

x_k = np.linspace(lower, upper, slices)
y_k = np.empty((slices), 'float32')
y_k2 = np.empty((slices), 'float32')
y_k1 = np.empty((slices), 'float32')

counter = 0

while(1):
        if counter == 0:
            y_k2[:] = 1.
            y_k = y_k2
        elif counter == 1:
            y_k1[:] = x_k[:]
            y_k = y_k1
        else:
            y_k = 2*x_k*y_k1 - y_k2
            y_k2 = y_k1
            y_k1 = y_k

        plt.ion()
        plt.ylim(-1., 1.01)
        plt.plot(x_k, y_k)
        plt.title("degree = " + str(counter))
        plt.show()
        try:
            key = input('To quit, enter ctrl-D; else return.')
            if not key:
                plt.clf()
        except EOFError:
            break
        counter += 1
