# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:57:39 2022

@author: Usuario
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Cargamos el conjunto de datos y separamos variable independientes y variables dependientes
dataset = pd.read_csv('cancer_de_cuello_uterino.csv')
a = dataset.iloc[:, :3].values
b = dataset.iloc[:,-1].values

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(datos_categoricos = [0])
a = onehotencoder.fit_transform(a).toarray()

"""
from sklearn.preprocessing import StandardScaler
sc_a = StandardScaler()
a_train = sc_a.fit_transform(a_train)
"""

