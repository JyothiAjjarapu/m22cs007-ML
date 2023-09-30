# -*- coding: utf-8 -*-
"""M22CS007_task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vUdLvyl__fzBe0RUPzokM27GKwRgVIad
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd

from random import seed
from random import randrange
from csv import reader
from math import exp

from google.colab import files
uploaded = files.upload()

import io
df = pd.read_csv(io.BytesIO(uploaded['imports-85.csv']))
df

columnnames=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors",
            "body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight",
            "engine-type",
            "num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
            "city-mpg","highway-mpg","price"]
df= pd.read_csv("imports-85.csv", header=None, names=columnnames )
df.head()

"""Data Cleaning by removing all the null rows"""

df=df.replace('?', np.NaN)
newdf=df.dropna()

data1=pd.get_dummies(newdf,columns=['make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels',
                                 'engine-location','engine-type','num-of-cylinders','fuel-system'], drop_first=True)
data1.head()

"""Taking Price as independent Variable"""

data1 = data1.astype('float')
x=data1.drop(['price'],axis=1)
y=data1['price']

train_size = int(0.7 * len(data1))

# Split your dataset 
train_set = data1[:train_size]
test_set = data1[train_size:]

x_t=train_set.drop(['price'],axis=1)
x_t[x_t.shape[1]]=1
y_t=train_set['price']

x_t=np.array(x_t)
y_t=np.array(y_t)


x_v=test_set.drop(['price'],axis=1)
x_v[x_v.shape[1]]=1
y_v=test_set['price']

x_v=np.array(x_v)
y_v=np.array(y_v)



x_t.shape

"""**Gardient descent function**"""

# cost function
def cost(x_data, params,y_data):
  total_cost=0
  for i in range(x_data.shape[0]):
    total_cost+=(1/x_data.shape[0])*((x_data[i]*params).sum()-y_data[i])**2
  return total_cost
  
#gardient descent
def gd(x_data,y_data,params,lr,iter_value):
  

  for i in range(iter_value):
    slopes=np.zeros(x_data.shape[1])
    for j in range(x_data.shape[0]):
      for k in range(x_data.shape[1]):
        slopes[k]  += (1/x_data.shape[0])*((x_data[j]*params).sum()-y_data[j])*x_data[j][k]
    params=params-lr*slopes
    # print(cost(x_data,params,y_data))
  return params

params=np.zeros(x.shape[1]+1)
lr=0.00000006
iter_val=5000
params=gd(x_t,y_t,params,lr,iter_val)
print(params)
print("loss in training =",cost(x_t,params,y_t))
print("loss in testing =",cost(x_v,params,y_v))

"""Both square mean loss is approximate same so not overfiting"""

total_cost=0
for i in range(x_v.shape[0]):
    total_cost+=((x_v[i]*params).sum()-y_v[i])**2
squared_error_regr=total_cost

y_mean=np.mean(y_v)

total_cost1=0
for i in range(x_v.shape[0]):
    total_cost1+=((x_v[i]*params).sum()-y_mean)**2
squared_error_mean=total_cost1


# r_square = coefficient_of_determination(ys,regression_line)
r_square= (1 - (squared_error_regr/squared_error_mean))
r_square

"""R square value is 0.41438 for my model."""