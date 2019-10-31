# -*- coding: cp1252 -*-
def ejercicio6():
    a=input("escribe un nº entero: ")
    b=input("escribe otro nº entero: ")
    repetir= True
    while (repetir== True):
        l=raw_input("ponga S para suma,R para resta,M para multiplicacion o D para division: ")
        if(l=='S' or l=='R' or l=='M' or l=='D'):
            repetir=False
        else:
            print "error ese comando no esta aceptado"

    if (l=='S'):
        print"Suma",a," + ",b,"=",a+b
    if (l=='R'):
        print"Resta",a," - ",b,"=",a-b
    if (l=='M'):
        print"SMultiplicación",a," x ",b,"=",a*b
    if (l=='D'):
        print"Division",a,"entre",b,"=",a/b
  



ejercicio6()
