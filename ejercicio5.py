# -*- coding: cp1252 -*-
def ejercicio5():
    a=input("introduzca una año: ")
    rmes=True
    rd=True
    while (rmes==True):
        m=input("introduzca una mes: ")
        rmes=((m<0)or(m>12))
        if (rmes==True):
            print m,"no es un mes"
    
    while (rd==True):
        d=input("introduzca un dia: ")
        rd=((d<0)or(d>31))
        if (rd==True):
            print d,"no es un dia"
    if (m==1):
         m="Enero"
    if (m==2):
        m= "Febrero"
    if (m==3):
        m= "Marzo"
    if (m==4):
        m= "Abril"
    if (m==5):
        m= "Mayo"
    if (m==6):
        m= "Junio"
    if (m==7):
        m="Julio"
    if (m==8):
        m= "Agosto"
    if (m==9):
        m= "Septiembre"
    if (m==10):
        m= "Octubre"
    if (m==11):
        m= "Noviembre"
    if (m==12):
        m="Diciembre"
    
    print d," de ",m," de ",a
    
    

ejercicio5()
