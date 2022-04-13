# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:22:37 2022

@author: Usuario

"""
import csv
import math

#Inciso A)



lista = []
with open('cancer_de_cuello_uterino.csv') as data:
    entrada=csv.reader(data)
    lista=list(entrada)
    
for linea in lista:
    print(linea)
    
#def calculate_percentile(linea, percentile):
#    size = len(linea)
#    return sorted(linea)[int(math.ceil((size * percentile) / 100)) - 1]

#percentile_25 = calculate_percentile(linea, 25)

#print("El primer cuartil es:",percentile_25)




#Inciso B)
from scipy import stats
import numpy as np #Matrices

file = 'cancer_de_cuello_uterino.csv'
data = np.genfromtxt('cancer_de_cuello_uterino.csv',delimiter=',', names= True,dtype=None)
print(data[:3])
print(data['Age'])
print("Percentil: ",np.percentile(data['Age'],50))


#data = np.recfromcsv(file)      #por fila
#print(data[:1])

#data = np.loadtxt(file,delimiter=',',skiprows=1,dtype=bytes).astype(str)
#print(data)
#print("Q1: ",np.percentile(data['Age'],50))



#print(array23)
#print(np.percentile(array23,50))

import pandas as pd
datos = pd.read_csv("cancer_de_cuello_uterino.csv", sep=",")
print(datos.head)
print(datos["Age"])
print("Q1",datos.quantile([0.25]))
print("Percentil:",np.percentile(datos["Age"],50))
df=pd.DataFrame(datos)
print("Q1: ",df['Age'],0.25)

#Inciso C)
grafica=df.boxplot()
