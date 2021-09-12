# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:18:39 2021

@author: bharathivts
"""

import pandas as pd

df =  pd.read_csv('balanced_reviews.csv')

df.shape

df.columns

df.sample(10)

df['reviewText'][0]

df['overall'].value_counts()

df.isnull().any(axis = 0)

df.dropna(inplace =  True)

df = df [df['overall'] != 3]

import numpy as np

df['Positivity'] = np.where(df['overall'] > 3 , 1 , 0)

#NLP

