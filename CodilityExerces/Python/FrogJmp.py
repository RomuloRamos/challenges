def FrogJmp(X,Y,D):
    
    intSteps = 0
    if((X>=0) and (Y>=X) and (D>0)):
        fDistance = (Y-X)
        if((fDistance % D) != 0):
            intSteps = int((fDistance/D)+1)
        else: 
            intSteps = int(fDistance/D)

    print("Quantidade de Saltos: ",intSteps)
    return intSteps


x = 10
y = 85
d = 30
FrogJmp(x,y,d) 