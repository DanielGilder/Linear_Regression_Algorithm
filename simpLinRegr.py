import numpy as np


class LinearRegression:

    
    global m, c

    def train(data):
        #x = np.array([1,2,3,4])  #InDependant variable  test example
        #y = np.array([1,2,3,4])  #Depdendendant variable test example

        x = data[:0]
        y = data[:,1]


        dy = ((np.mean(x) * np.mean(y)) - np.mean(x*y))
        dx = ((np.mean(x)**2) - np.mean(x*y))

        m = dy/dx
        print(m)
        c = np.mean(y) - m * np.mean(x)
        print(c)

    
    def predict(x):
        print((m*x) + c)
        return ((m*x) + c)
    





