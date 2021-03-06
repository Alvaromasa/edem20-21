#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:09:24 2021

@author: alvaro
"""

import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 


os.chdir('/Users/alvaro/Desktop/archive')
os.getcwd()

wbr = pd.read_csv ("student-mat.csv", sep=',', decimal=',')
wbr.shape
wbr.head()

print(wbr.Walc)

print(wbr.Walc.describe())

x=wbr['Walc']


#  grafico de barras alcohol jovenes 

plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(1,6,step=1))
plt.title("figura 1. registro alcohol jovenes")
plt.ylabel('frecuencia')
plt.show()



mytable = wbr.groupby(['guardian']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100

print(round(mytable2,1))


bar_list = ['father','mother','other']


plt.bar(bar_list,mytable2,edgecolor='black')
plt.ylabel('percentaje')
plt.title('percentaje of guardian')
plt.text(1.7, 50,'n: 395')
plt.show()


print(wbr.groupby('studytime').Walc.mean())

cnt_ml= wbr.loc[wbr.studytime==1,"Walc"]
cnt_l= wbr.loc[wbr.studytime==2,"Walc"]
cnt_h= wbr.loc[wbr.studytime==3,"Walc"]
cnt_vh= wbr.loc[wbr.studytime==4,"Walc"]

res=stats.f_oneway(cnt_ml,cnt_l,cnt_h,cnt_vh)

# el pvalue es 0.00000 por lo que es significativo 
print(res)




plt.figure(figsize=(5,5))
ax = sns.pointplot(x="studytime", y="Walc",
data=wbr,ci=95, join=0)
plt.yticks(np.arange(0, 5, step=1))
plt.ylim(0,5)
plt.axhline(y=wbr.Walc.mean(),
linewidth=1,
linestyle= 'dashed',
color="blue")
plt.title('Figure 6. Average walc by study time.''\n')
plt.show()



# Compramos en función del sexo



sex_femin= wbr.loc[wbr.sex=="F","Walc"]
sex_masc= wbr.loc[wbr.sex=="M","Walc"]

res=stats.ttest_ind(sex_femin, sex_masc,equal_var=False)
print(res[1])

plt.figure(figsize=(5,5))
ax = sns.pointplot(x="sex", y="Walc",
data=wbr,ci=95, join=0)
plt.yticks(np.arange(0, 5, step=1))
plt.ylim(0,5)
plt.axhline(y=wbr.Walc.mean(),
linewidth=1,
linestyle= 'dashed',
color="blue")
plt.title('Figure 6. Average walc by genre.''\n')
plt.show()


# Comparamos el consumo de alcohol en fin de semana en función del estado de salud --> 1 muy mala; 5 muy buena

print(wbr.groupby('health').size())

health_mm= wbr.loc[wbr.health==1,"Walc"]
health_m= wbr.loc[wbr.health==2,"Walc"]
health_n= wbr.loc[wbr.health==3,"Walc"]
health_b= wbr.loc[wbr.health==4,"Walc"]
health_mb= wbr.loc[wbr.health==5,"Walc"]

res=stats.f_oneway(health_mm,health_m,health_n,health_b,health_mb)

# el pvalue es 0.14 por lo que no es significativo 
print(res)

plt.figure(figsize=(5,5))
ax = sns.pointplot(x="health", y="Walc",
data=wbr,ci=95, join=0)
plt.yticks(np.arange(0, 5, step=1))
plt.ylim(0,5)
plt.axhline(y=wbr.Walc.mean(),
linewidth=1,
linestyle= 'dashed',
color="blue")
plt.title('Figure x. Average walc by health.''\n')
plt.show()



# Comparamos el consumo de alcohol entre semana en función del estado de salud --> 1 muy mala; 5 muy buena


print(wbr.groupby('health').size())

health_mm= wbr.loc[wbr.health==1,"Dalc"]
health_m= wbr.loc[wbr.health==2,"Dalc"]
health_n= wbr.loc[wbr.health==3,"Dalc"]
health_b= wbr.loc[wbr.health==4,"Dalc"]
health_mb= wbr.loc[wbr.health==5,"Dalc"]

res=stats.f_oneway(health_mm,health_m,health_n,health_b,health_mb)

# el pvalue es 0.38 por lo que no es significativo el consumo de alcohol entre semana con la salud
print(res)

plt.figure(figsize=(5,5))
ax = sns.pointplot(x="health", y="Walc",
data=wbr,ci=95, join=0)
plt.yticks(np.arange(0, 5, step=1))
plt.ylim(0,5)
plt.axhline(y=wbr.Walc.mean(),
linewidth=1,
linestyle= 'dashed',
color="blue")
plt.title('Figure x. Average Dalc by health.''\n')
plt.show()


# vamos a comparar ahora a la edad con el consumo de alcohol en fin de semana de 15 a 19 años
print(wbr.groupby('age').size())

health_mm= wbr.loc[wbr.age==15,"Walc"]
health_m= wbr.loc[wbr.age==16,"Walc"]
health_n= wbr.loc[wbr.age==17,"Walc"]
health_b= wbr.loc[wbr.age==18,"Walc"]
health_mb= wbr.loc[wbr.age==19,"Walc"]
health_20= wbr.loc[wbr.age==20,"Walc"]
health_21= wbr.loc[wbr.age==21,"Walc"]
health_22= wbr.loc[wbr.age==22,"Walc"]


res=stats.f_oneway(health_mm,health_m,health_n,health_b,health_mb,health_22,health_21,health_20)

# el pvalue es 0.006 por lo que es significativo el consumo de alcohol en findes en funcion de la edad
print(res)

plt.figure(figsize=(5,5))
ax = sns.pointplot(x="age", y="Walc",
data=wbr,ci=95, join=0)
plt.yticks(np.arange(0,7, step=1))
plt.ylim(0,6)
plt.axhline(y=wbr.Walc.mean(),
linewidth=1,
linestyle= 'dashed',
color="blue")
plt.title('Figure x. Average Dalc by health.''\n')
plt.show()
