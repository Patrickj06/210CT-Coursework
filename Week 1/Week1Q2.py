
from Error import  ErrorPrevention  #Imported function i wrote for error detection
def factorialZero(x):
    '''A function that works out the number of trailing zeros of a factoiral number
    by using the prime factors of 5 to work it out '''
    done = False
    i = 5
    zeros = 0
    while done != True:             #Loops until it can not find any more multipules of 5  
        multFive = x//i             #Divides the number the user inputed,x, and divides
        zeros = multFive + zeros    #by a multipule of 5 
        if multFive == 0:
            done = True
        else:
            i = i * 5               #i increase by increments of 5^n
    return zeros

done = False
while done != True:
    num = input("Please enter a number :")
    Test = ErrorPrevention(num,int,"ERROR - Please enter a vaild number")
    if Test == True:
        done = True
        
Zeros = factorialZero(int(num))
print("There are ",Zeros, "0's in" , num, "factorial")


    
