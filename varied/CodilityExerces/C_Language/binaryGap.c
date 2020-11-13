/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

//Binary Gap

#include <stdio.h>

char fCountBinaryGap(int iNumber){
    
    int iHandleInput = iNumber;
    char cCounter = 0;
    char cBinaryGap = 0;
    char cFlag = 0;
    char cNumberOfBitToCheck = 32; //lengh of int type
    
    for(int iLoopCounter = 0 ; iLoopCounter < cNumberOfBitToCheck; iLoopCounter++){
        if( (iHandleInput >> iLoopCounter) & (1)){
            if(cFlag == 0) cFlag =1;
            else{
                if(cCounter > cBinaryGap) cBinaryGap = cCounter;
                cCounter = 0;
            }
        }
        else{
            if(cFlag){
                cCounter++;
            }
        }
    }    
    
    return cBinaryGap;
}



int main()
{
    int iValueToTest = 0x38018001;
    
    printf("Value Found was: %d", fCountBinaryGap(iValueToTest));
    
    return 0;
}
