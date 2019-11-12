# -*- coding: cp1252 -*-
def ajedrez():
    n=input("pon el nº de filas: ")
    a='*'
    b="0"
    for i in range(1,n+1):
            if(i%2==0):
                print (b+a)*(n/2)
            else:
                print (a+b)*(n/2)
       
ajedrez()
