#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 20:31:25 2021

@author: alvaro
"""

import os
import pandas as pd    # gestionar datasets
import numpy as np     #gestionar numeros
import matplotlib.pyplot as plt      #  hacer gráficos

os.chdir('/Users/alvaro/Desktop/pythonestadistica/data')
print(os.getcwd())

wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';' , decimal=',')
print(wbr.head(3))


## selecccioar variables
my_vars=['temp_celsius','cnt']
wbrminimal = wbr[my_vars]

mytable = wbr.groupby(['yr']).size()

wbryr= wbr[wbr.yr==0]



wbryr2012= wbr[wbr.yr==1]
wbrmonth = wbryr2012[wbr.mnth == 9 & 10 & 11 & 12]



wbrotom= wbr[(wbr.season == 3) | (wbr.season==1)]
plt.hist(wbrotom.cnt)




