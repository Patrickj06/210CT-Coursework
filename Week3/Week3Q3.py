
def removeVowel(string):
    '''Recusive function that removes all vowels from a string
    and returns the string.'''
    Vowels = ["A","E","I","O","U","a","e","i","o","u"]
    if len(string) == 0:                #Base case if the string equals 0 the return the string
        return string
    else:
        newString = string[1:]          #Cuts out first letter of string
        letter = string[0]              #Current letter checking
        if letter in Vowels:            #If letter is vowel the dont add it back
            return removeVowel(newString)
        else:
            return letter + removeVowel(newString)

user_input = input("Please enter a word :")
print(removeVowel(user_input))
