
"""
Created on Fri Nov 12 16:49:47 2021

@author: alvaro
"""

import os
import pandas as pd    # gestionar datasets
import numpy as np     #gestionar numeros
import matplotlib.pyplot as plt      #  hacer gráficos

os.chdir('/Users/alvaro/Desktop/pythonestadistica/data')
print(os.getcwd())

rentals2011 = pd.read_csv('washington_bike_rentals_2011.csv', sep=';' , decimal=',')
print(rentals2011.head(3))

#QC ok

print(rentals2011.cnt)

print(np.mean(rentals2011.cnt))
print(np.std(rentals2011.cnt))

print(rentals2011.cnt.describe())

#print(plt.hist(rentals2011.cnt))

#variables cuantitativas(media,desviacion y histograma)
      
x=rentals2011['cnt']

plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(0,7000,step=1000))
plt.title("figura 1. registro rentals washington")
plt.ylabel('frecuencia')
plt.show()


weather2011 = pd.read_csv('weather_washington_2011.csv', sep=';' , decimal=',')
print(rentals2011.head(3))
#QC OK

print(weather2011.dtypes)
#juntar dos variables 
weatherrentals2011= pd.merge(weather2011,rentals2011, on="day")

#guardar a un csv 
weatherrentals2011.to_csv("weatherrentals.csv")

# borrar la variable 
del weatherrentals2011['dteday_x']

#cambiar nombre una columna 
weatherrentals2011 = weatherrentals2011.rename(columns={"dteday_y":"fecha"})

# añadir filas por debajo para añadir 
rentalsweather2012 = pd.read_csv("rentals_weather_2012.csv", sep=';' , decimal=',')

rentasweather1112 = weatherrentals2011.append(rentalsweather2012)

rentasweather1112 = weatherrentals2011.append(rentalsweather2012,ignore_index=True)

wbr = rentasweather1112

del (rentasweather1112)
del (weatherrentals2011)
del (rentals2011)
#tabla de las variables a estudiar los cuales son cualitativos 
mytable = wbr.groupby(['weathersit']).size()

print(mytable)

#sumar los numeros de la variable

n= (mytable.sum())

#hacer los porcentajes

mytable2 = (mytable/n)*100
print(mytable2)

#redondear a un decimal 

print(round(mytable2,1))


bar_list = ['Sunny','Cloudy','rainy']

plt.bar(bar_list,mytable2,edgecolor='black')
plt.ylabel('percentaje')
plt.title('percentaje of weather situation')
plt.text(1.7, 50,'n: 731')


plt.savefig('bar1.svg')
plt.savefig('bar1.jpg')

print(wbr.tail())













































