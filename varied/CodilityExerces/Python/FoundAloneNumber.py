def foundNumberAlone(A):

    B = []
    intCounterA = 0
    print("Composiçao de B: ", B)
    print("Composiçao de A: ", A)  

    for aux in A:
        print("Trabalhanco com: ", aux)
        if (len(B) != 0):
            intCounterB = 0
            for bAux in B:
                print("Indexador de B: ", intCounterB)
                if aux == bAux:
                    print("O item retirado foi: ", aux)
                    B.pop(intCounterB)
                    B.sort()
                    print("Nova composiçao de B: ", B)
                    break
                elif (intCounterB == (len(B)-1)):
                    B.append(aux)
                    B.sort()
                    print("Nova composiçao de B: ", B)
                    print("O item inserido foi: ", aux)
                    break
                intCounterB = intCounterB+1
        else: 
            print("Acionando o valor: ", aux)
            B.append(aux)

    print("O valor encontrado foi: ", B[0])            

array = [2,5,4,2,7,5,4]
foundNumberAlone(array)