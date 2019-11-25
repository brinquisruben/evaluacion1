# -*- coding: cp1252 -*-
def pajarita2():
    n=input("nº: ")
    ast="*"
    esp=" "
    for i in range (1,n+1):
        a=ast*(i)+esp*((n)-i)
        b=esp*((n)-i)+ast*i
        print a+b
    
    for x in range(1,n+1):
        c=ast*((n)-(x-1))+esp*(x-1)
        d=esp*(x-1)+ast*(n-(x-1))
        print c+d
        








pajarita2()
