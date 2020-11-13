/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

//Rotate Array A[], with lengh N, K times

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Results {
  int * A;
  int N; // Length of the array
} tstrResults;

void fRotateArray(int A[], int N){
    
    printf("\nArray Recebido na funcao2: ");    
    for(int iCount = 0; iCount < N; iCount++){
        printf("%d", A[iCount]);
    }
    if(N > 1 ){
        int iAux = A[0];
        int iAuxTemp = 0;
        for(int iCount = 1 ; iCount < N ; iCount++){
            iAuxTemp = A[iCount];
            A[iCount] = iAux;
            iAux = iAuxTemp;
            printf("\nA[iCount]: %d", A[iCount]);
            if((iCount+1) == N)A[0] = iAux;
        }
    }
}

tstrResults fRotateArraySeveralTimes(int A[], int N, int K){
    
    printf("\nArray Recebido na funcao: ");    
    for(int iCount = 0; iCount < N; iCount++){
        printf("%d", A[iCount]);
    }
    
    tstrResults  strResult;
    int iShiftQuantity = 0;
    
    int *iArray = malloc(N * sizeof (int));
    memcpy(iArray, A, (sizeof(int))*N);
    printf("\niArray: ");    
    for(int iCount = 0; iCount < N; iCount++){
        printf("%d", iArray[iCount]);
    }
    strResult.A = iArray;
    strResult.N = N;
    
    if(K > N) iShiftQuantity = K % N;
    else iShiftQuantity = K;
    
    for(int iCount = 0; iCount < iShiftQuantity; iCount++){
        
        fRotateArray(iArray, N);
    }
    printf("\niArray Novo: ");    
    for(int iCount = 0; iCount < N; iCount++){
        printf("%d", strResult.A[iCount]);
    }
    return strResult;
}

int main()
{
    int A[5];// = {3,8,9,7,6};
    A[0] = 3; A[1] = 8; A[2] = 9; A[3] = 7; A[4] = 6; 
    int N = sizeof(A)/sizeof(int);
    printf("Array enviado: ");    
    for(int iCount = 0; iCount < N; iCount++){
        printf("%d", A[iCount]);
    }
    tstrResults strResult = fRotateArraySeveralTimes(A, N, 1);

    printf("\nArray resultante: ");    
    for(int iCount = 0; iCount < N; iCount++){
        printf("%d", strResult.A[iCount]);
    }
    
    return 0;
}
