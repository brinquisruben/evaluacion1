# -*- coding: cp1252 -*-
def ejercicio4():
    repetir=True
    while(repetir==True):
        mes= input("introduzca nº de mes: ")
        repetir=((mes<0)or(mes>12))
        if (repetir==True):
                 print"Error"
                 
    if (mes==1):
        print "Enero"
    if (mes==2):
        print "Febrero"
    if (mes==3):
        print "Marzo"
    if (mes==4):
        print "Abril"
    if (mes==5):
        print "Mayo"
    if (mes==6):
        print"Junio"
    if (mes==7):
        print "Julio"
    if (mes==8):
        print "Agosto"
    if (mes==9):
        print "Septiembre"
    if (mes==10):
        print "Octubre"
    if (mes==11):
        print "Noviembre"
    if (mes==12):
        print "Diciembre"
ejercicio4()
    
    
          
        
