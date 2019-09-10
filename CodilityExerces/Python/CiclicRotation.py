def ciclicRotation(A,K):
    if((K>0) and (len(A)>0)):
        print("A: ", A)
        intShift = (K % len(A))#5
        print("intShift: ", intShift)
        intToCopy = (len(A) - intShift)#2
        print("intToCopy: ", intToCopy)
        intPos = ((intShift-1) - (intToCopy-1))#POSICAO 3
        if(intPos < 0):
            intPos = ((intToCopy-1) - (intShift-1))
            print("intPos: ", intPos)
    #        B = list(A[intShift:])#B = [5,6]
            B = (list(A[intToCopy:]))+(list(A[0:intToCopy]))
            print("B: ", B)
        else:
            B = list(A[intShift:])#B = [5,6]
            print("intPos: ", intPos)
        #        B = list(A[intShift:])#B = [5,6]
            print("B: ", B)
            B = (list(A[intToCopy:intShift]))+B+(list(A[0:intToCopy]))#B = [5,6,0,1]
            print("B: ", B)
        
        return B    
    else:
        return A






A = [0,1,2,3,4,5,6,9,10]
ciclicRotation(A, 100)