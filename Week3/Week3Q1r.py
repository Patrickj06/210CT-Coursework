
def ReverseString(wordArray):
    '''Recursive function that take a parameter, type:array, and  
    reverses the order of the words '''
    if len(wordArray) == 1:     #Base case if there is one item in array then return the array
        return wordArray
    else:
        word = [wordArray[-1]]
        return word + ReverseString(wordArray[:-1]) #calling function in its self and returning back the 
                                                    #retured array plus the last element of that saved possition
string = input("Please enter a sentence :")
Array = string.split(" ")

print(' '.join(ReverseString(Array)))   #Coverets an array to string 



