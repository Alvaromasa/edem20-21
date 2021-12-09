#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 19:30:45 2021

@author: alvaro
"""

import os
import pandas as pd    # gestionar datasets
import numpy as np     #gestionar numeros
import matplotlib.pyplot as plt      #  hacer gráficos
import seaborn as snb

os.chdir('/Users/alvaro/Desktop/pythonestadistica/data')
print(os.getcwd())

studentP= pd.read_csv('StudentsPerformance.csv', sep=';')
print(studentP.head(3))
print(studentP.readingscore.describe())
print(studentP.writingscore.describe())
print(studentP.mathscore.describe())

x=studentP['readingscore']
plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(0,105,step=5))
plt.title("figura 1. Notas reading")
plt.ylabel('frecuencia')
plt.show()

y=studentP['mathscore']
plt.hist(y,edgecolor='black',bins=20)
plt.xticks(np.arange(0,105,step=5))
plt.title("figura 1. Notas math")
plt.ylabel('frecuencia')
plt.show()

course_gender = studentP.groupby(['gender']).mean()

print(course_gender)




