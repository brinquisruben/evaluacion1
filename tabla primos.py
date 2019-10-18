def tabla_primos():
    nprimero= input("1ER numero")
    nfinal=input("hasta que numero quiere que cuente: ")
    primo=True
    for i in range(nprimero,nfinal+1):
        for a in range(2,i):
            if(i%a==0):
                primo=False
        if(primo==True):
            print i,"primo"
        else:
            print i,"no primo"
        primo=True   


tabla_primos()    
