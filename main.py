from simpLinRegr import LinearRegression
import numpy as np

data = np.array([[1,2,3,4],[1,2,3,4]])

model = LinearRegression()
model.train(data)
