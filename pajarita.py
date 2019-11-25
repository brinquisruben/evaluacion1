# -*- coding: cp1252 -*-
def pajarita():
    n= input("nº columnas que se desea: ")
    ast="*"
    esp=" "
    for pisos in range(1,n+1):
        d=esp*(pisos-1)+ast*(n-(pisos-1))
        c= ast*(n-(pisos))+esp*(pisos-1)
        print d+c
    for altura in range(1,n+1):
        a=esp*(n-altura)+ast*altura
        b=ast*(altura-1)+esp*(n-altura)
        print a+b
    
            
       
    

pajarita()
