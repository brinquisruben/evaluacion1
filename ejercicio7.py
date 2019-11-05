# -*- coding: cp1252 -*-
def ejercicio7():
    repetir=True
    while (repetir==True):
        l=raw_input("ponga S para suma,R para resta,M para multiplicacion o D para division: ")
        if (l=='S' or l=='R' or l=='D' or l=='M'):
            repetir=False
        else:
            print "error esa letra no es aceptada"
    if (l=='S'):
        a=input("pon un nº: ")
        b=input("pon otro nº: ")
        print"Suma",a," + ",b,"=",a+b
    if (l=='R'):
        a=input("pon el primer nº que quieres restar")
        b=input("pon el  nº que quieres restar al anterior")
        print"Resta",a," - ",b,"=",a-b
    if (l=='M'):
        a=input("pon un nº: ")
        b=input("pon otro nº: ")
        print"Multiplicación",a," x ",b,"=",a*b
    if (l=='D'):
        a=input("pon el numerador: ")
        repetir2= True
        while (repetir2==True):
            b=input("pon el denominador: ")
            if b==0:
                print "error"
            else:
                repetir2=False
        print"Division",a,"entre",b,"=",a/b
ejercicio7()
