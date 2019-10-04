#en este programa le pedimos al usuario que introduzca
#los coefiicentes de un polinomio y hayamos el valor de las
#raices
import math
def calculatorpolimios():
    print "introduzca los coeficientes del polinomio"
    print "A*xx+b*x+c=0"
    a=input("A= ")
    b=input("B= ")
    c=input("C= ")
    radicando=b*b-4*a*c
    if (radicando>0):
        raiz1=(-b- math.sqrt(radicando))/(2*a)
        raiz2=(-b+ math.sqrt(radicando))/(2*a)
        print " solucion 1"
        print  raiz1
        print "solucion2"
        print  raiz2
    else:
        print "No tiene solucion real"
    

calculatorpolimios()
