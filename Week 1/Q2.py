def factorialZero(x):
    done = False
    i = 5
    zeros = 0
    while done != True:
        multFive = x//i
        zeros = multFive + zeros
        if multFive == 0:
            done = True
        else:
            i = i * 5
        
    print("There are ",zeros, "0's in" , x, "factorial")

num = int(input("Please enter a number :"))
factorialZero(num)
