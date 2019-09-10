import sys


def binaryGap(N):
    print("Numero passado: ", N)
    strNumber = bin(N)
    print("Valor em binário: ",strNumber)
    bMarkerInit = False
    intCounterIteration = 0
    intCounterZeros = 0
    intMaxFound = 0

    for aux in strNumber:
        print(aux)
        intCounterIteration = intCounterIteration+1
        if aux == 'b':
            bMarkerInit = True
        elif bMarkerInit == True:
            if aux == '1':
    #           if bMarkerInit == False:
    #               bMarkerInit = True
    #               intCounter = 0
    #           else:
                if intCounterZeros > intMaxFound:
                    intMaxFound = intCounterZeros
                    print("Maior valor temporario: ", intMaxFound)
                intCounterZeros = 0 
            else: 
                intCounterZeros = intCounterZeros+1

    return intMaxFound        


binaryGap(197)