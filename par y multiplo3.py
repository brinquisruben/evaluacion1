# -*- coding: cp1252 -*-
def par_y_divisble_para_tres():
    a= input("introduzca nº: ")
    if(a%2==0):
        if(a%3==0):
            print "multiplo de 2 y 3"
        else:
            print "par y no multiplo de 3"
    else:
        if(a%3==0):
            print "impar y multiplo de 3"
        else:
            print "impar y no multiplo de 3"

par_y_divisble_para_tres()
