# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 01:32:17 2022

@author: Usuario
"""
import pandas as pd
from sklearn import tree
from sklearn import datasets as ds
examen = ds.load_wine()
print(examen)
clasificador = tree.DecisionTreeClassifier()
print(clasificador)
x=[[18,15,34],
   [4.0,1.0,1.0],
   [15.0,14.0,0],
   [1.0,1.0,1.0],
   [0.0,1,0.0]]
y=['Age', 'Number of sexual partners', 'First sexual intercourse', 'Num of pregnancies','Smokes']
resultado=clasificador.fit(x,y)
yp=clasificador.predict([[1.0,1.0,1.0],[4.0,1.0,1.0]])
print(yp)

