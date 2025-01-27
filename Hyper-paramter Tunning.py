# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kNpHKH2gU_k3ylTzEmCUs6vLJaVHNvfR
"""

#import all necessary library
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
import keras
from keras.models import Sequential
from keras.layers import Dense

#load data and seperate Dependent and Independent 
data=load_breast_cancer()
X=data.data
Y=data.target

#explore the data
print(X)

#explore the target
print(Y)

#what is to be classify
print(data.target_names)
#the objective is to predict the type of cancer using ANN/MLP
#class to predict is :['malignant' 'benign']

#we will split data for training stage and testing stage as we ANN comes under Supervised Stage
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=.30,random_state=42)

#lets start forming our ANN model With 1 Hidden Layer
#make model from keras
model=Sequential()

#first Hidden Layer
model.add(Dense(16,kernel_initializer='glorot_uniform',activation='relu',input_dim=30))
#hidden layer nodes input/2 number

#2nd hidden layer
model.add(Dense(16,kernel_initializer='glorot_uniform',activation='relu'))

#Output Layer
model.add(Dense(1,kernel_initializer='glorot_uniform',activation='sigmoid'))

#model compile
model.compile(optimizer='Adam',loss='binary_crossentropy',metrics=['accuracy'])

#model train on training Datasets
model.fit(x_train,y_train,batch_size=100,epochs=150)

#lets predict the test datasets
pred=model.predict(x_test)
#we will predict on x_test and compare with y_test for analysis
#lets generate a threshold value where acuuracy is maximum
#lets say if pred>0.5 its 1 else 0
prediction=[]
for i in pred:
   if(i>0.5):
     prediction.append(1)
   else:
     prediction.append(0)

from sklearn.metrics import accuracy_score
print("ANN Accuracy is :",accuracy_score(y_test,prediction))

#ANN Accuracy is : 0.9649122807017544

#K-Fold Cross Validation
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
import keras
from keras.models import Sequential
from keras.layers import Dense
#def a function which will evaluate accuarcy on different folds
def cross_model():
   model=Sequential()
   model.add(Dense(16,kernel_initializer='glorot_uniform',activation='relu',input_dim=30))
   model.add(Dense(16,kernel_initializer='glorot_uniform',activation='relu'))
   model.add(Dense(1,kernel_initializer='glorot_uniform',activation='sigmoid'))
   model.compile(optimizer='Adam',loss='binary_crossentropy',metrics=['accuracy'])
   return model

model=KerasClassifier(build_fn=cross_model,batch_size=100,epochs=100)
accuracies=cross_val_score(estimator=model,X=x_train,y=y_train,cv=10,
                           n_jobs=-1)

print(accuracies)

print(accuracies.mean())
#the avg accuarcy of model can be 89.70%

print(accuracies.std())

#Hyper-paramter tunning
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import keras
from keras.models import Sequential
from keras.layers import Dense
#def a function which will evaluate accuarcy on different folds
def model1(optimizer='Adam'):
   model=Sequential()
   model.add(Dense(16,kernel_initializer='glorot_uniform',activation='relu',input_dim=30))
   model.add(Dense(16,kernel_initializer='glorot_uniform',activation='relu'))
   model.add(Dense(1,kernel_initializer='glorot_uniform',activation='sigmoid'))
   model.compile(optimizer=optimizer,loss='binary_crossentropy',metrics=['accuracy'])
   return model

model=KerasClassifier(build_fn=model1)
para={'batch_size':[100,150],'epochs':[100,200],'optimizer':['Adam','rmsprop']}
gs=GridSearchCV(estimator=model,param_grid=para,
               scoring='accuracy',cv=10)

gs.fit(x_train,y_train)

print("Best Parameter is :",gs.best_params_)
print("Best Score is :",gs.best_score_)