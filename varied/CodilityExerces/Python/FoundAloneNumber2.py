def foundNumberAlone(A):

    print("Composiçao de A: ", A)  
    
    intCounter = 1
    while(intCounter < len(A)):
        print("Tamanho de A é: ", len(A))
        if A[0] == A[intCounter]:
            print("O item retirado foi: ", A[intCounter])
            A.pop(intCounter)
            A.pop(0)
            A.sort()
            print("Nova composiçao de A: ", A)
            intCounter = 1
        else:    
            intCounter = intCounter+1

    print("O valor encontrado foi: ", A[0])



array = [2,5,4,2,7,5,4]
foundNumberAlone(array)