# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:48:00 2021

@author: bharathivts
"""

import pandas as pd

dataset = pd.read_csv("student_scores.csv")

dataset.shape
dataset.columns

dataset.isnull().any(axis = 0)


features = dataset['Hours'].values

labels = dataset['Scores'].values


import matplotlib.pyplot as plt
plt.scatter(features,labels)
