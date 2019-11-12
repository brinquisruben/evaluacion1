def piramide():
    asterisco="*"
    espacio=" "
    pisos=input("numero de pisos: ")
    for altura in range(1,pisos+1):
        c=espacio*(pisos-altura)+asterisco*(altura)
        d=asterisco*(altura-1)+espacio*(pisos-altura)
        print c+d
       
            
   
            













piramide()
