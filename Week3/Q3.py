
def removeVowel(string):
    Vowels = ["A","E","I","O","U","a","e","i","o","u"]
    if len(string) == 0:
        return string
    else:
        letter = string[0]
        newString = string[1:]
        if letter in Vowels:
            return removeVowel(newString)
        else:
            return letter + removeVowel(newString)

user_input = input("Please enter a word :")
print(removeVowel(user_input))
