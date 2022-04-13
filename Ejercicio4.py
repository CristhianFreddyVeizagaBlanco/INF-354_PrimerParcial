# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 00:13:51 2022

@author: Usuario
"""
from kanren import run, var, eq, Relation, facts
a = var()
b = var()
c = var()
d = var()
e = var()
f = var()

padre = Relation()
madre = Relation()
hermano = Relation()
abuelo = Relation()
tio = Relation()
primo = Relation()
#Papá
facts(padre, ("Fernando","Cristhian"),("Fernando","Jason"),("Serafin","Fernando"))
facts(padre, ("David","Kiko"),("David","Isarrael"),("papa","David"))
#Mamá
facts(madre, ("Justina","Cristhian"),("Justina","Jason"),("Juana","Justina"))
#Hermano
facts(hermano, ("Justina","Cristhian"),("Justina","Jason"),("Cristhian","Jason"))
facts(hermano, ("David","Fernando"),("Fernando","David"))

#Abuelo
facts(abuelo, ("Serafin","Cristhian"),("Serafin","Jason"),("Serafin","Cristhian"))
#Tio
facts(tio, ("David","Cristhian"),("David","Jason"),("tio","David"))
#Primo
facts(primo, ("Kiko","Cristhian"),("Kiko","Jason"),("primo","Kiko"))
#print(padre.facts)

print("Padre de Cristhian es ",run(1,a,padre(a,"Cristhian")))
print("El padre de Fernando es ",run(1,a,padre(a,"Fernando")))
print("Justina es madre de ",run(2,b,madre("Justina",b)))
print("Son hermanos ",run(3,c,hermano("Justina",c)))
print("Abuelo de Cristhian es ",run(4,d,abuelo(d,"Cristhian")))
print("Tio de Jason es ",run(5,e,tio(e,"Jason")))
print("Primo de Cristian es ",run(6,f,primo(f,"Cristhian")))





