#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:15:27 2022

@author: samantha
"""

import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv')  

type(df)

df.head()
df.tail()
df.shape
df.duplicated().sum()

df.info()
df.isna().sum()
df.describe()
df.describe(include = 'all')
df.nunique()

df['parental level of education'].unique()
df.gender.value_counts()

provas = ['math score', 'reading score', 'writing score']
df.sort_values(['math score']).reset_index(drop = True)

df = df.sort_values(by = provas, ascending = False).reset_index(drop = True)

df['mean'] = df[provas].mean(axis = 1)

# consulta
df.query('(gender == "male") & (`test preparation course`  == "none") & (`math score` >= 70)')

df[(df.gender == 'male') & (df['test preparation course'] == 'none') & (df['math score'] >= 70)]

df.loc[(df.gender == 'male') & (df['test preparation course'] == 'none') & (df['math score'] >= 70)]

df.groupby(by = 'gender')[provas].agg([np.mean, np.median]).T































