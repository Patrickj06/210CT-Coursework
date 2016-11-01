
def ReverseString(wordArray):
    if len(wordArray) == 1:
        return wordArray
    else:
        
        return wordArray[-1] + ReverseString(wordArray[:-1])




string = input("Please enter a sentence :")
Array = string.split(" ")
print(ReverseString(Array))



