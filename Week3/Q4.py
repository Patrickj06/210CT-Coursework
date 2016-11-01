import random
cubes = []
n = 20
colours = ["Red","Blue","Yellow","Green","Purple"]
for i in range(n):
    num1 = random.randint(0,4)
    num2 = random.randint(1,20)
    string = colours[num1]  , num2
    cubes.append(string)

def Tower(Cubes):
    

