import random

def shuffle(numList):
    for i in range(len(numList)+100):
        x = random.randint(0,len(numList) - 1)
        y = random.randint(0,len(numList) - 1)
        temp = numList[x]
        numList[x] = numList[y]
        numList[y] = temp
        
List = [1,2,3,4,5,6,7,8,9]
shuffle(List)
print(List)


