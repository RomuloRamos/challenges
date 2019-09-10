def TapEquilibrium(A):
    
    N = len(A)
    intSmalestModule = 999999999

    for P in range(N):
        print("P = ", P)
        intPart1 = sum(list(A[:(P+1)]))
        print("intPart1 = ", intPart1)
        intPart2 = sum(list(A[(P+1):]))
        print("intPart2 = ", intPart2)
        intModule = intPart1 - intPart2
        
        if (intModule < 0):
                intModule*=(-1)  
        
        if (intSmalestModule > intModule):
                print("intModule = ", intModule)
                intSmalestModule = intModule

        print("intSmalestModule = ", intSmalestModule)        
        print("intModule = "+ str(intModule)+ "\n")

    return intSmalestModule




print("Teste de TapEquilibrium\n")

A = [3,1,2,4,3]
print("Teste com A = ", A)
print("TapEquilibrium(A) = ",TapEquilibrium(A))

A = [-1000,-1000]
print("Teste com A = ", A)
print("TapEquilibrium(A) = ",TapEquilibrium(A))

A = [0,1,2,3,4,-5]
print("Teste com A = ", A)
print("TapEquilibrium(A) = ",TapEquilibrium(A))