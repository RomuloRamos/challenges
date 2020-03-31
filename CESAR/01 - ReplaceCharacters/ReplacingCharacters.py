def replaceSpaces(strArray):

    print("Your string was: ", strArray)
    return strArray.replace(" ", "&32")


if __name__ == "__main__":

    print("Please, enter with your string:")
    strList = input()    

    print("Your new Array is: ", replaceSpaces(strList))