def checkWordsTypos(str1, str2):

    if(abs(len(str1)-len(str2)) > 1):
        return False

    intCount1 = 0
    intCount2 = 0
    intErrors = 0
    intMaxErrors = 1
    if (len(str1) < len(str2)):
        intErrors += 1
    while intCount1 < len(str1):

        # if last character was removed
        if(intCount2 >= len(str2)):
            # boolTypoRemove = True
            intErrors += 1    
        elif(str1[intCount1] != str2[intCount2]):
            intErrors += 1
            if(str1[intCount1+1] == str2[intCount2]):
                # boolTypoRemove = True
                intCount1 += 1       
        intCount1 += 1 
        intCount2 += 1 
        if(intErrors > intMaxErrors):
            return False

        
    return True

if __name__ == "__main__":

    while 1:
        print("Please, enter with firt string:")
        strList1 = input()    
        print("Please, enter with secound string:")
        strList2 = input()   

        print("Validation result is: ", checkWordsTypos(strList1, strList2))