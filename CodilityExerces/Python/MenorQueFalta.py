A = [23,2,4,1,43,65,32,1,7]
print("A sequencia original é: ", A)
A.sort()
print("A sequencia em ordem fica: ", A)
marker_low = A[0]
marker_hi = A[(len(A)-1)]
print("O menor elemento é: ", marker_low)
print("O maior elemento é: ", marker_hi)

##B = range(marker_low,(marker_hi+1))

counter = marker_low

for aux in A:
    if aux == (counter-1):
        pass
    elif counter != aux:
        print("O menor valor que falta é: ", counter)
        print("O ultimo valor em sequência foi: ", (aux-1))
        print("O valor que saltou foi: ", aux)
        break   
    else:
        counter = counter+1
