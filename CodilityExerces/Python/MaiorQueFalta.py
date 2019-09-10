A = [152,23,153,154,33,65,4,2,1,3]
print("A lista original é: ", A)
A.sort(reverse = True)
print("A lista ordenada inversamente fica: ", A)

marker_hi = A[0]
print("Inicio do marcador: ", marker_hi)
for aux in A:
    if aux < marker_hi:
        print("O valor esperado era: ",marker_hi)
        print("O valor na posiçao da lista é: ",aux)
        marker_hi = (aux-1)
    elif aux == marker_hi:
        marker_hi = marker_hi-1
    elif aux > (marker_hi+1):
        print("Erro")    