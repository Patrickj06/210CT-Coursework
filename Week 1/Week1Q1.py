import random

def shuffle(numList):
    '''Function that randomly shuffles a list. numList is a list and the function
    will create an error if it isn't'''
    for i in range(len(numList)+100):
        x = random.randint(0,len(numList) - 1)  #Generates two random numbers that are the positions 
        y = random.randint(0,len(numList) - 1)  #of the locations in the list

        temp = numList[x]                       #Swaps the two locations around 
        numList[x] = numList[y]
        numList[y] = temp

    return numList
        
List = [1,2,3,4,5,6,7,8,9]
print(shuffle(List))



