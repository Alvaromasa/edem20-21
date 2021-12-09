#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:30:47 2021

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

### Computing new columns
wbr['cs_ratio'] = (wbr.casual)/(wbr.registered)

wbr.cs_ratio.describe()
#plt.hist(wbr.cs_ratio)






mytable = pd.crosstab(index=wbr["workingday"],
columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])



print(wbr.groupby('workingday').cnt.mean())

cnt_wd= wbr.loc[wbr.workingday==1,"cnt"]
cnt_nwd= wbr.loc[wbr.workingday==0,"cnt"]

res=stats.ttest_ind(cnt_wd, cnt_nwd,equal_var=False)
print(res[1])



plt.figure(figsize=(5,5))
ax = sns.pointplot(x="workingday", y="cnt",
data=wbr,ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=wbr.cnt.mean(),
linewidth=1,
linestyle= 'dashed',
color="blue")
props = dict(boxstyle='round',facecolor='white', lw=0.5)
plt.text(0.85,5400,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 6. Average rentals by Working Day.''\n')
