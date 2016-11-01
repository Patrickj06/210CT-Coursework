'
def ReverseString(string):
    word = ""
    wordArray = []
    rString = ""
    for i in range(len(string)):
        word = word + string[i]
        if (string[i] == " ") or (i == len(string)-1):
            wordArray.append(word)
            word = ""

    for i in range(len(wordArray),0,-1):
        rString = rString + " " + wordArray[i-1]  
        
    print(rString)
s = input("Please enter a sentence :")
ReverseString(s)
