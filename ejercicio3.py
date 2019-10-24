def ejercicio3():
    repetir=True
    while(repetir==True):
        diasemana= input("Introduzca dia de la semana en numero: ")
        repetir=(diasemana<0) or (diasemana>7)
        if(repetir==True):
            print("ERROR. Ese dia no existe. ")
    if (diasemana==1):
        print "Lunes"
    if (diasemana==2):
        print "Martes"
    if (diasemana==3):
        print "Miercoles"
    if (diasemana==4):
        print "Jueves"
    if (diasemana==5):
        print "Viernes"
    if ( (diasemana==6)or(diasemana==7)):
        print "fin de semana"
        if (diasemana==6):
             print "sabado"
        else:
            print "domingo"

ejercicio3()
