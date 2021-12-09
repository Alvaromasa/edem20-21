


#SESIÓN 4


import os                              #sistema operativo
import pandas as pd                    #gestionar dataframes
import numpy as np                     #numeric python vectores
import matplotlib.pyplot as plt        #graficos

os.chdir('/Users/alvaro/Desktop/pythonestadistica/data')
os.getcwd()
wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv',sep=';', decimal= ',')
wbr.shape
print(wbr.tail())

wbr.cnt.describe()

wbr.cnt

#SUBSETTING significa seleccionar columnas, SELECTING VALARIABLES

#PRIMERO DEFINIMOS MI LISTA DE VARIABLES CON LAS QUE VAMOS A TRABAJAR
my_vars=['temp_celsius','cnt']

wbr_minimal = wbr[my_vars]
wbr_minimal .shape

wbr_minimal.to_csv('wbr_minimal_edem2020.csv')

#explore year
mytable = wbr.groupby(['yr']).size()
print(mytable)

#Percentajes



wbr_2011 = wbr[wbr.yr == 0]

plt.hist(wbr_2011.cnt)
wbr_2011.cnt.describe()


#EJERCICIO1. DESCRIBE BIKE RENTALS IN THE INTER OF 2012
wbr_2012_winter = wbr[(wbr.yr == 1) & (wbr.season == 1)]  #subseting with 2 conditions
wbr_2012_winter.shape


plt.hist(wbr_2012_winter.cnt)
plt.title("Rentals in winter 2012")
wbr_2012_winter.cnt.describe()

#EJERCICIO 1B. bike rentals en inbvierno y otoño
wbr_fall_winter = wbr[(wbr.season ==1) | (wbr.season == 4) ]  #como se pone la barra vertical en python? significa 'or' en python
wbr_fall_winter.shape

plt.hist(wbr_fall_winter.cnt)
plt.title("Rentals in Fall & Winter 2011-2012")
wbr_fall_winter.cnt.describe()


import os                              #sistema operativo
import pandas as pd                    #gestionar dataframes
import numpy as np                     #numeric python vectores
import matplotlib.pyplot as plt        #graficos

os.chdir(r'C:\Users\luiso\OneDrive\Escritorio\EDEM21-22\Fundamentos\estadistica\data_1_3')
os.getcwd()

wbr_ue= pd.read_csv ('wbr_ue.csv',sep=';', decimal= ',')

my_vars=['temp_celsius']

wbr_temp = wbr_ue[my_vars]
wbr_temp.describe()

plt.hist(wbr_temp)


wbr_ue['temp_celsius_c'] = wbr_ue.temp_celsius.replace(99,np.nan)  # nan= nunpay not a number, porque en esos casos habian errores y no vaale el dato, es la manera de poner que no tengo informacion
#he creado una nueva columna de temperatura donde cuando ocurra lod e los 99 grados, se cambiará 'nan' con el replace

wbr_ue.temp_celsius_c.describe()
plt.hist(wbr_ue.temp_celsius_c)



wbr_ue.temp_celsius_c.dropna() #    ue solo coja datos validos y elimine los nans
plt.hist(wbr_ue.temp_celsius_c)

wbr_ue.temp_celsius_c.describe()

wbr_ue2 = wbr_ue.dropna()

print(wbr_ue.shape)
print(wbr_ue2.shape)




import os                              #sistema operativo
import pandas as pd                    #gestionar dataframes
import numpy as np                     #numeric python vectores
import matplotlib.pyplot as plt        #graficos

os.chdir(r'C:\Users\luiso\OneDrive\Escritorio\EDEM21-22\Fundamentos\estadistica\data_1_3')
os.getcwd()
wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv',sep=';', decimal= ',')
wbr.shape
print(wbr.tail())

wbr.cnt.describe()

wbr['cs_ratio']=(wbr.casual)/(wbr.registered)
wbr.cs_ratio.describe()
plt.hist(wbr.cs_ratio)


del(wbr['cnt'])

wbr['cnt']= wbr.casual + wbr.registered   #metodo robusto para llamar a columnas
#1 invierno, 2 primavera, 3 verano y 4 otoño



#Siempre que hagamos una recodificación hay que hacer quality control
#RECODE--> RECODIFICAR

#RECODING SEASON INTO A STRING VARIABLE (SEASON_CAT)

wbr = wbr.drop(columns="season_cat") #Como eliminar otra columna con otra sintaxis



wbr.loc[(wbr['season']==1),"season_cat"]="Winter" #coordenada x y coordenada y, la coordenada vertical y la horizonntal.
wbr.loc[(wbr['season']==2),"season_cat"]="Spring"
wbr.loc[(wbr['season']==3),"season_cat"]="Summer"
wbr.loc[(wbr['season']==4),"season_cat"]="Autum"

#Quality control
pd.crosstab(wbr.season, wbr.season_cat) #tabla cruzada de la  variable original contra la nueva
#QC OK

#Recoding of rentals into ordinal
res = wbr['cnt'].describe()
print(res)
#Store parameters as numbers
m = res[1]
sd = res[2]
n = res[0]


print("Lower limit:", round(m-sd,0))
print("Upper limit:", round(m+sd,0))



wbr.loc   [  (wbr['cnt']<2567),"cnt_cat2"]="1: Low rentals" #coordenada x y coordenada y, la coordenada vertical y la horizonntal.
wbr.loc   [  ((wbr['cnt']>=2567) & (wbr['cnt']<6442)),"cnt_cat2"]="2: Average rentals" #aqui estamos transformando cualquier rango de valores en un nuevo valor
wbr.loc   [  (wbr['cnt']>=6442),"cnt_cat2"]="3: High rentals"

#QC

plt.scatter(wbr.cnt, wbr.cnt_cat2)




