# -*- coding: cp1252 -*-
#programa que va a decir si es primo o no
def primo_no_primo():
    a=input("introduzco un nº")
    primo= True
    for i in range(2,a):
        if(a%i==0):
            primo= False
        else:
            primo= True
    if( primo==True):
        print "es primo"
    else:
        print"no primo"
        
     
primo_no_primo()       
