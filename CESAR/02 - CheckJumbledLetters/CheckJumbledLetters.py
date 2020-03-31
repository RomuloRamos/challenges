def checkJumbledLetters(str1, str2):
    if (str1[0] != str2[0]):
        return False
    
    intMaxChange = int((2/3)*len(str1))
    print("Max changed positions:", intMaxChange)
    intCount = 0
    intChanges = 0
    while intCount <= len(str1):
        if(str1[intCount] != str2[intCount]):
            intChanges+=1
        if intChanges>intMaxChange:
            return False
        intCount += 1 

    return True

if __name__ == "__main__":

    while 1:
        print("Please, enter with firt string:")
        strList1 = input()    
        print("Please, enter with secound string:")
        strList2 = input()   

        print("Validation result is: ", checkJumbledLetters(strList1, strList2))