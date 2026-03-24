#Basic perceptron initial code 
#only single layer perceptron
# activation function as STEP function if Z >= 0 then 1 else 0

import numpy as np

def step(x):
    if x > 0:
        return 1
    else:
        return 0

"""
for each 
    w = [0,0]
    b = -1.5
    z = 1*0 + 1*0 - 1.5 ( w1*x1 + w2*x2 + b -> )
"""


alpha = 0.01
iters = 1000
weights = None
bias = None

logic = [[0,0],[0,1],[1,0],[1,1]]

def fit(X , y , alpha = 0.01 , epochs = 1000):
    n_samples , n_features = X.shape
    

