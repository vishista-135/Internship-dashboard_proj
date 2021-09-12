# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:54:08 2021

@author: bharathivts
"""

import pandas as pd

dataset = pd.read_csv("student_scores.csv")


#split the data in two sets
#train set - training the model 60 - 80%
#test set - we evaluate how good or bad your model is 40 - 20% 
#train test split



features = dataset['Hours'].values

labels = dataset['Scores'].values

##perform it (train test split)


from sklearn.model_selection import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)

from sklearn.linear_model import LinearRegression

#create object
regressor = LinearRegression()

#model
features_train = features_train.reshape(20,1)

regressor.fit(features_train, labels_train)

features_test = features_test.reshape(5,1)

pred = regressor.predict(features_test)



pd.DataFrame(zip(pred, labels_test))
#score
#train score
regressor.score(features_train, labels_train)
#predict(features_train)
#compare with labels_train

#test score


regressor.score(features_test, labels_test)




data = pd.read_csv('cricket_salary_data.csv')

data.isnull().any(axis = 0)

#imputation
#SimpleImputer

features = data.iloc[:,0:3].values

labels = data.iloc[:,3].values

from sklearn.impute import SimpleImputer

from numpy import nan

imputer = SimpleImputer(missing_values = nan, strategy = 'mean')

features[:,1:2] = imputer.fit_transform(features[:,1:2])