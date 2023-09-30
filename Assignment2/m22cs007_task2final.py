# -*- coding: utf-8 -*-
"""M22CS007_Task2final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/101MXC1Jra9LjX-4Z_Zkys9oSQFbgSAs_

Part (a): Use Principal Component Analysis (PCA) to reduce the dimensionality of the dataset. Inbuilt
libraries can be used for the same.
"""



"""# PCA

Dataset: Human Activity Recognition with Smartphones - 
Loading the data
"""

import numpy as mp
# import numpy 
import pandas as sw
# import andas
import matplotlib.pyplot as sun
# import matplotlib
from google.colab import files
uploaded = files.upload()
# choosing the files to upload it to colab

# import io to read the dataset
import io
coc= sw.read_csv(io.BytesIO(uploaded['train.csv']))
# read csv is used
coc

coc.head()
# just viewing top 5 rows

# Import necessary libraries

import seaborn as ffd # for heat maps
from sklearn.preprocessing import StandardScaler # for standardizing the features
from sklearn.decomposition import PCA # for PCA
import pandas as sw # for dataframes

# import pandas library
import pandas as sw


# this is dictionary file
Activity_modified = {'WALKING': 2, 'WALKING_DOWNSTAIRS':4,'STANDING': 1, 'SITTING':5, 'WALKING_UPSTAIRS':3,'LAYING':6}

# looking dataframe coc
# For the values for which the key matches, we are looking for
coc.Activity = [Activity_modified[it] for it in coc.Activity]
print(coc)

#Features stadardizing
#From sklearn.preprocessing, we use standard scaler library for creating object
scr = StandardScaler()
scl_coc = sw.DataFrame(scr.fit_transform(coc)) 
#data is being scaled
scl_coc

# Co-relation between features without PCA
ffd.heatmap(scl_coc.corr())

#Now applying PCA
#Taking no. of Principal Components as 3
m=3
pca = PCA(n_components = m)
# making it fit to our pca data i.e scl_coc which is scaled
pca.fit(scl_coc)
#transforming it
coc_pca = pca.transform(scl_coc)
# creating a dataframe for the pca data generated
coc_pca = sw.DataFrame(coc_pca,columns=['PCmp1','PCmp2','PCmp3'])
# viewing its top 5 rows
coc_pca.head()

# plotting the pca data using heatmap from matplotlib
ffd.heatmap(coc_pca.corr())

# describing the pca data
coc_pca.describe()

# shape of the pca data
coc_pca.shape

"""Plotting the pca data

# Kmeans from task 1
"""

"""KMeans from scratch

Importing required libraries like numpy , pandas, matplotlibrary as mp, sw, sun"""


import numpy as mp
import pandas as sw
import matplotlib.pyplot as sun



"""Now printing the data that we read from local storage"""

coc_pca

coc_pca1=coc_pca[['PCmp1','PCmp2']]
coc_pca1

"""Now, normalizing and splitting the data using standard scaler function from sklearn preprocessing module(library)

I made 80:20 split.and used random state 25
"""

z=0.8
g=25

from sklearn.preprocessing import StandardScaler
XTrain = coc_pca1.sample(frac=z, random_state=g)
XTrain= StandardScaler().fit_transform(XTrain)

X=mp.array(XTrain)

"""printing the shape of Xtrain"""

print(XTrain.shape)

"""In the shape function, first attribute means the no. of training samples or examples and y atttribute means the columns. I took tem into 2 variables m and n respectively"""

XTrain_rows=XTrain.shape[0] 
#number of training examples
n=XTrain.shape[1] 
#number of features. Here n=2

#printing m
XTrain_rows

"""I want to run this code for 300 iteration, so I kept noof iterations as 300."""

noofiterations=300

"""Initialised no. of clusters , k to be 2. because no. of labels in the outcome column or attribute is 2. {1,0} """

k=2

"""Now, I created an array for centroids. anyway this centroid array keeps updating after completing the set of iterations it stops. """

CentroidsArray=mp.array([]).reshape(n,0)

"""Printing the empty array."""

CentroidsArray

"""Now, I am randomly initializing the Cluster centers. For this, using randint fuction from numpy."""

import random as v

i=0
while i<k:
   
   rd=v.randint(0,XTrain_rows-1)
   # random initialization of clusters centroids
   CentroidsArray=mp.c_[CentroidsArray,X[rd]]
   # adding it to array
   # incrementing loop variable
   i=i+1

"""Now, After initializing random centroids, lets see what are the centroids. so printing them"""

print(CentroidsArray)

"""Now, we should perform distance metric. Kmeans uses Euclidean distance. so, seeing what are the available vectors to perform distance measurement. Xtrain, and centroidsArray we will be using. SO printing them"""

XTrain

CentroidsArray

"""Creating a output variable, for printing, I will use later."""

Opt={}

"""Now, creating an array to store the distances. and is initialised with size of m (no. of training examples)"""

EuclidianDistance=mp.array([]).reshape(XTrain_rows,0)

# import math as math
h=0
mt=2
re=1
while h<k:
  diff=X-CentroidsArray[:,h]
  # finfing diff btween centroids and points
  buffer=mp.sum((diff)**mt,axis=re)
  # square them and sum them
  # store in buffer
  EuclidianDistance=mp.c_[EuclidianDistance,buffer]
# adding it to array
  C=mp.argmin(EuclidianDistance,axis=re)+re
  # C is the minimum of all the distances
  h=h+re
# increment loop variable
#compute the clusters
Y={}
re=1

j=0
while j<k:
    Y[j+re]=mp.array([]).reshape(2,0)
    # computing Y[j+re]
    #using reshape and array functions
    j=j+re
   # computing j again

o=0
while o<XTrain_rows:
    Y[C[o]]=mp.c_[Y[C[o]],X[o]]
    # computing Y[] gain with c
    o=o+re
  # computing o
 

w=0
while w<k:
  Y[w+re]=Y[w+re].T
  # computing Y using y[w+re] and tranforming it
  w=w+re
 
d=0
while d<k:
  CentroidsArray[:,d]=mp.mean(Y[d+re],axis=0)
  # computing centroids Array 
  d=d+re
# computing d




"""For iterations, we repeat these 2 steps again and again"""
from os import read
# imported read from os

e=0
while e<noofiterations:
  #Step 1
  EDce=mp.array([]).reshape(XTrain_rows,0)
  #this is Euclidean distance array
  # we are repeating the same steps here als
  # so initializing a,mt, re

  a=0
  mt=2
  re=1
  while a<k:
    diff=X-CentroidsArray[:,a]
    # finding the diff btwen centroid and point
    ds=(diff)**mt
    # multiplying with itself or squaring
    buffer=mp.sum(ds,axis=re)
    # storing in buffer
    # sqbuffer=math.sqrt(buffer)
    # and adding these to array
    EDce=mp.c_[EuclidianDistance,buffer]
    C=mp.argmin(EuclidianDistance,axis=re)+re
    # computing C , a, and e
    a=a+re
  e=e+re;

#step 2
Y={}
j=0
#computing j
while j<k:
  # finding Y[j+re]
  # using reshape
    Y[j+re]=mp.array([]).reshape(2,0)
    j=j+re
    #finding j

i=0
while i<XTrain_rows:
  # initialised i
  # Finding Y[C[i]]
    Y[C[i]]=mp.c_[Y[C[i]],X[i]]
    i=i+re

w=0
while w<k:
  # again Y
  Y[w+re]=Y[w+re].T
  #transpose it
  w=w+re
  # fid w

d=0
while d<k:
  #computing centroids array
  CentroidsArray[:,d]=mp.mean(Y[d+re],axis=0)
  d=d+re
  # got d

Opt=Y
# finally assigning Y to output and printing it
Y

#Scatter plot
import matplotlib.pyplot as sctplt

sctplt.scatter(X[:,0],X[:,1],c='black',label='data which is not clustered yet')

# scattreplot of 1st column and 2nd column, basically bp and insulin inthis case
sctplt.title('Plot of data points')
# giving title as plot of data points
sctplt.legend()
# and showing or displaying it
sctplt.show()


"""Now, plotting the clustered data

We have 2 clusters, so using 2 colors to show them
"""
# initialised colors and labels
color=['red','cyan']
labels=['cluster1','cluster2']

eq=0 
re=1
while eq<k:
  
  # now plotting the graph on clustered data
  sctplt.scatter(Opt[eq+re][:,0],Opt[eq+re][:,1],
              c=color[eq],
              label=labels[eq])
  eq=eq+re
  
sctplt.scatter(CentroidsArray[0,:],CentroidsArray[1,:],marker="*",s=200,c='black',label='Centroids')

sctplt.legend()
# showing it
sctplt.show()

"""## **Kmeans on pca dataset using inbuilt libraries**"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.cluster import KMeans
from sklearn import preprocessing
import sklearn.cluster as cluster
import sklearn.metrics as metrics

from sklearn.preprocessing import MinMaxScaler
import seaborn as ffd
from matplotlib import pyplot as sunplt
# %matplotlib inline

coc_pca.head()

coc_pca.shape

scr = MinMaxScaler()
scale = scr.fit_transform(coc_pca[['PCmp1','PCmp2','PCmp3']])
df_scale = sw.DataFrame(scale, columns = ['PC1','PC2','PC3']);
df_scale.head(5)

m=2
km=KMeans(n_clusters=m)
y_predicted = km.fit_predict(coc_pca[['PCmp1','PCmp2','PCmp3']])
y_predicted

km.cluster_centers_

coc_pca['Clusters'] = km.labels_
ffd.scatterplot(x="PCmp1", y="PCmp2",hue = 'Clusters',  data=coc_pca,palette='viridis')



"""# GMM using task1 algorithm"""

import numpy as mp
import pandas as sw
import matplotlib.pyplot as sun



"""Now printing the data that we read from local storage"""

coc_pca

coc_pca1=coc_pca[['PCmp1','PCmp2']]
coc_pca1

#importing sklearn standardscalar
# for doing scaler operation

from sklearn.preprocessing import StandardScaler
 # using standard scaler fro standardising
XTrain = coc_pca1.sample(frac=0.8, random_state=25)
# i used 80:20 split
XTrain= StandardScaler().fit_transform(XTrain)
# finally using this to apply on Xtrain

# converting ths to array
X=mp.array(XTrain)

from numpy.lib import dstack
#importing dstack from numpy.lib
from numpy.core.function_base import linspace
# importing linspace
import numpy as mp
import matplotlib.pyplot as plt
from scipy.stats.stats import WeightedTauResult
from scipy.stats import multivariate_normal
# importing multivariate_normal from scipystats for guassian distribution calculations

#GMM application to our data
#Initializing noofclusters
# to be 2 and iterations 
#to be 20 for our model

noofclusters = 2
mxitr = 20

def gmm_plot(X,noofclusters=2,mxitr=20):

        """lets initialize the parameters
         and then 
         perform E step and M step 
         by lets also store log-likelihood 
         values after every iteration"""

        # we have to compute pi, mean, variance

        # pi = no.of clusers in that k/total no. of clusters
        re=1
        pi = mp.full(shape=noofclusters, fill_value=re/noofclusters)
       
        # We can calculate mean (mu) using this equation
        # mu = np.random.randint(min(X[:, t]), max(X[:, t]), size=(noclusters, len(X[t]))) where t=0

        gmmdata = X.shape
        
        #storing X shapein gmmdata
        X_rw, ft_col = gmmdata

        # We can print shape for our convinence

        t=0
        rw_rd = mp.random.randint(low=t, high=X_rw, size=noofclusters)

        #creating an empty array let it be buffer
        buffer=[]
        
        for b in range(len(rw_rd)):
          buffer.append(X[b,:])
          # appending X[b,:] to buffer
        buffer
        #print(buffer)
        # printing buffer for my convinience, but need not print actualy
        mvu=buffer
        # So assigning it to mean mvu
        # print(mvu)
        # not needed

  #calculated mean mvu
  #now time for covvariance

        d=0
        cvvarian = mp.zeros((noofclusters, len(X[d]), len(X[d])))
        # creating a covvariance matrix,
        # actally an empty array firstly
       
        a=0
        w=5
        # assigned a=0, w=5

        while a <len(cvvarian):
            mp.fill_diagonal(cvvarian[a], w)
            a=a+1
          
          # we are filling the diagonal as 0, because the covvariace of itself is always 0.
          # here we can use .eye() function also, instead of writing fill_diagonal and all that. both gives the same result

        # reg_cov is used for numerical stability i.e. 
        #to check singularity issues in covariance matrix

        v=1e-6
        # this is the minum element
        covvarian_reg = v*mp.identity(len(X[a]))
        # so this will fill out the covariance of remaining values

        x,y = mp.meshgrid(mp.sort(X[:,0]), mp.sort(X[:,1]))
        # creating a meshgrd, 
        # to sort x and y values

        GH = mp.array([x.flatten(), y.flatten()]).T
      # converted as per requirement and storing in GH

        # data plotting and the initial model

        
        fig0 = plt.figure(figsize=(10,10))
        a0 = fig0.add_subplot(111)
        a0.set_title("Intial figure")
        a0.scatter(X[:, 0], X[:, 1])
       
       
        for k, l in zip(mvu, cvvarian):
            l += covvarian_reg
            multi_guass = multivariate_normal(mean=k, cov=l)
            a0.contour(mp.sort(X[:, 0]), mp.sort(X[:, 1]), multi_guass.pdf(GH).reshape(len(X), len(X)), colors = 'black', alpha = 0.3)
            a0.scatter(k[0], k[1], c='red', zorder=10, s=100)
        
      
        plt.show()
#plotting the graph

      #creating a array for calculating log likelikhood

        log_liklihods = []

        
        s=0
        # initialised s
        # Starting of GMM actually

        while s < mxitr:

            # E-Step

            ric = mp.zeros((len(X), len(mvu)))
            # inialising ric with length of x and mean

            for pic, muc, covc, r in zip(pi, mvu, cvvarian, range(len(ric[0]))):
              # pic,muc,covc,r are the loop variables here
              # they match to Pi, mean and covvariance above

                covc += covvarian_reg
                # addition of covc with values of covvariance_reg
                mn = multivariate_normal(mean=muc, cov=covc)
                # assigning the guassian of mean and covvariance function to mn.
                # now, multiplying this pic (basically the mixing coefficient with probability distribution function of guassian)
                ric[:, r] = pic*mn.pdf(X)

           
            k=0
            # initialised K to 0
            while k<len(ric):
              # when its within the loop, divide the value that we got with sum of all the values of that dataset
              # just following the formula in E step
                ric[k, :] = ric[k, :] / mp.sum(ric[k, :])
                k=k+1
                # incrementing the looping variable

            # M-step

            # in M step, we generally reassign the parameters

            mc = mp.sum(ric, axis=0)
            # mixing coefficient pi, mc/mp.sum(mc)
            pi = mc/mp.sum(mc)
            # again mean 
            mu = mp.dot(ric.T, X) / mc.reshape(noofclusters,1)
            # again covariance
            cov = []

            count=0
            # initialised count
            while count < len(pi):
              #simple covariance formula in multivariate guassian

                covc = 1/mc[count] * (mp.dot( (ric[:, count].reshape(len(X), 1)*(X-mu[count]) ).T, X - mu[count]) + covvarian_reg)
                # finding for every value and appending it to covariance array
                cov.append(covc)
                # incrementing the count
                count=count+1

            # converting this covariance vector to array
            cov = mp.asarray(cov)
            
            # the main thing would be log likelihood calculation
            # find multivariate guassian for mean, covariance and the sum it up by taking the multiple of pi
            likelihood_sum = mp.sum([pi[r]*multivariate_normal(mu[r], cov[r] + covvarian_reg).pdf(X) for r in range(len(pi))])
            # this should repeat for len(pi) times
            log_liklihods.append(mp.sum(mp.log(likelihood_sum)))
            
            # plotting the figures
            f1 = plt.figure(figsize=(10,10))
            # axis1 is subplot of actual figure
            a1 = f1.add_subplot(111)
            #These are subplot grid parameters encoded as a single integer. 
            # For example, "111" means "1x1 grid, first subplot" and "234" means "2x3 grid, 4th subplot".
            a1.scatter(X[:, 0], X[:, 1])
            # scatter plot of 2 features that we considered
            # title is kept using iteration
            # as it runs for some iterations, and corresponding iteration name is printed
            a1.set_title("Iteration " + str(s))


            q=100
            y=10
            # plotting again 
            for m, c in zip(mu, cov):
              # adding covariance reg to c
                c += covvarian_reg
                # finding guassian of mean and variance and assigning it to a variable
                multi_normal = multivariate_normal(mean=m, cov=c)
                # we need those rings, so this is the code

                a1.contour(mp.sort(X[:, 0]), mp.sort(X[:, 1]), multi_normal.pdf(GH).reshape(len(X), len(X)), colors = 'red', alpha = 0.3)
                # scatter plot again
                a1.scatter(m[0], m[1], c='black', zorder=y, s=q)
            
           # pplot again and display
            plt.show()
            # incrementing the loop variable
            s=s+1
            
        # now we are plotting for log likelihood of the model
        f=111
        s=s-1
        # decrementing the loop varible
        f2 = plt.figure(figsize=(y,y))
        # again taking the subplot of 1x1 grid , first plot
        ax2 = f2.add_subplot(f)
        # plot for log likelihood
        ax2.plot(range(0, s+1, 1), log_liklihods)
# this is the title
        ax2.set_title('Plot of loglikelihood ')
       
        plt.show()
# display the plot

cx=2
gf=15

# finally calling the gmm method, giving 2 clustes and 15 iterations as input 
gmm_plot(X,2,15)





"""## **GMM on data_pca using libraries**"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as ffd; ffd.set()
import numpy as np

from sklearn.mixture import GaussianMixture

ndarray = coc_pca.to_numpy()

ndarray

gm = GaussianMixture(n_components=3, random_state=0).fit(ndarray)
gm.means_

labels = gm.predict(ndarray)
plt.scatter(ndarray[:, 0], ndarray[:, 1], c=labels, s=40, cmap='viridis');
