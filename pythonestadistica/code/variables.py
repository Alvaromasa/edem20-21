#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 18:29:14 2021

@author: alvaro
"""

import os                              #sistema operativo
import pandas as pd                    #gestionar dataframes
import numpy as np                     #numeric python vectores
import matplotlib.pyplot as plt        #graficos
from pandas.api.types import CategoricalDtype
import scipy.stats as stats
import seaborn as sns


os.chdir('/Users/alvaro/Desktop/pythonestadistica/data')
os.getcwd()

wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';',decimal = ',')

"""
mytable = pd.crosstab(index=wbr["workingday"],
columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])


#Descriptive comparison:
wbr.groupby(['yr']).size()



#Statistical comparison:
#Extract the two sub samples and store them in two objects
cnt_year11=wbr.loc[wbr.yr==0, "cnt"]
cnt_year12=wbr.loc[wbr.yr==1, "cnt"]
#Perform a t test for mean comparison



import seaborn as sns

import scipy.stats as stats  #sirve para hacer estadísticas
stats.ttest_ind(cnt_year11, cnt_year12, equal_var = False)  #cuando se comparen las medias le pido a python que sea conservador

res= stats.ttest_ind(cnt_year11, cnt_year12, equal_var = False)

print(res[1])





plt.figure(figsize=(5,5))
ax = sns.pointplot(x="workingday", y="cnt", data=wbr,ci=95, join=0)

#ajustar eje eje y
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)                                                            #Limite

#Pintar linea en la media
plt.axhline(y=wbr.cnt.mean(),
linewidth=1, linestyle= 'dashed', color="green")

#Caja de texto
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(0.85,5400,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)

#Texto ejes
plt.xlabel('Working Day')
plt.ylabel('Rentals')
plt.title('Figure 6. Average rentals by Working Day.''\n')
"""


mytable = pd.crosstab(index=wbr["weathersit"],
columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])


#Descriptive comparison:
wbr.groupby(['weathersit']).size()



#Statistical comparison:
#Extract the two sub samples and store them in two objects
cnt_sol=wbr.loc[wbr.weathersit==1, "cnt"]
cnt_nub=wbr.loc[wbr.weathersit==2, "cnt"]
cnt_ll=wbr.loc[wbr.weathersit==3, "cnt"]
#Perform a t test for mean comparison

res=stats.f_oneway(cnt_sol, cnt_nub, cnt_ll)
print(res)

"""import seaborn as sns

import scipy.stats as stats  #sirve para hacer estadísticas
stats.ttest_ind(cnt_sol, cnt_nub, cnt_ll, equal_var = False)  #cuando se comparen las medias le pido a python que sea conservador

res= stats.ttest_ind(cnt_year11, cnt_year12, equal_var = False)

print(res[1])

"""


#plt.hist(cnt_sol,cnt_nub,cnt_ll)


plt.figure(figsize=(5,5))
ax = sns.pointplot(x="weathersit", y="cnt", data=wbr,ci=95, join=0)

#ajustar eje eje y
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(1000,6200)                                                            #Limite

#Pintar linea en la media
plt.axhline(y=wbr.cnt.mean(),
linewidth=1, linestyle= 'dashed', color="green")

#Caja de texto
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(0.85,5400,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)

#Texto ejes
plt.xlabel('Working Day')
plt.ylabel('Rentals')
plt.title('Figure 6. Average rentals by Working Day.''\n')
plt.show()
ax = sns.boxplot(x="weathersit", y="cnt", data=wbr)

