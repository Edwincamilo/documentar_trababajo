# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 17:11:01 2021

@author: 57314
"""
print("ingrese 3 numeros enteros diferenetes") #se le dice a la persona lo que debe ingresar
e = int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor")) # se le indica las dos opciones a elegir
a = int(input("ingrese el numero a")) #se le indica que ingrese el primer numero
b = int(input("ingrese el numero b")) #se le indica que ingrese el segundo numero
c = int(input("ingrese el numero c")) #se le indica de ingrese el tercer numero

if (e == 1): # primera condicion igual a 1 donde el usuario elige si quiere ordenar de menor a mayor
    if (a > b): # primer numero a > que el numero b
        if (a > c): #primer numero a > que el numero c
            if(b > c): #segundo numero b > que numero c
               print(a, b, c) # muestra el resultado 
            else:# si no se cumplen se pasa a la siguiente condicion 
               print(a, c, b) # se muestran los numeros digitados por la persona
    if (c > a): # si numero c > que el numero a
        if (c > b): # si numero c > que el numero b
            if(b > a): #si numero b > que el numero a
               print(c, b, a) # se muestra el resultado de los numeros digitados 
            else: # si no se cumple la condicion se pasa a la siguiente condicion
               print(c, a, b) # se muestran los numero digitados por la persona 
    if (b > a): #si numero b > que numero a
        if (b > c): # si numero b > que numero c
            if(a > c): # si numero a > que numero c
               print(b, a, c) # se muestra resultado de los numeros digitados
            else: # si no se cumple la condicion se pasa a la siguiente condicion 
               print(b, c, a) # se muestran los numeros digitados por la persona 


if (e == 2): # segunda condicion igual a 2 donde el usuario elige si quiere ordenar de mayor a menor 
    if (a < b): # primer numero a < que numero b
        if (a < c): # primer numero a < que numero c
            if(b < c): # segundo numero b < que numero c
               print(a, b, c) #muestra el resultado al usuario de los numeros digitados
            else: # si no se cumple la condicion se pasa a la siguiente condicion 
               print(a, c, b) # se muestran los numeros dijitados por la persona 
    if (c < a): # si numero c < que numero a
        if (c < b): # si numero c < que numero b
            if(b < a): # si numero b < que numero a
               print(c, b, a) # se muestra el resultado de los numeros digitados 
            else: # si no se cumple la condicion se pasa a la siguiente condicion
               print(c, a, b) # se muestran los numeros digitados por la persona 
    if (b < a): # si numero b < que numero a 
        if (b < c): # si numero b < que nuermo c
            if(a < c): #si numero a < que numero c
               print(b, a, c) # se muestra el resultado de los numeros digitados 
            else: # si no se cumple la condicion se pasa a la siguiente 
               print(b, c, a)# se muestan los numeros digitados por la persona

if (a == b): # si a es igual a b
    print("b y a son iguales") # indica que b y a son iguales
    if (a == c): # si a  es igual c 
        print("a y c son iguales") # indica que a y c son iguales
        if(b == c): # si a es igual a b
           print(" b y c con iguales") # indica que b y c son iguales
           if(a == b == c): # si a  es igual a b e igual a c 
              print("todos son iguales") # indica que todas las variables son iguales