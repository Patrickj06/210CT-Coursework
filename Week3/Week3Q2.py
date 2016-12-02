
def primeNumber(n,test):
    '''Recusive function to check if the integer is a prime number
    parameters: n is a the number that is being tested and test is the number it is testing it againist
    '''
    if test == n:           #Base case if the testing number equals 
        return True         #the number inputed then it is a prime
    if n % (test) == 0:     #mod tell us that if 0 then it goes into it 
        return False
    elif n % (test) != 0:   
        return primeNumber(n,test+1) # call function again adding 1 to test number

number = int(input("Please enter number :"))
output = primeNumber(number,2)

if output == False:
    print(number, " is not a prime number")
else:
    print(number, "is a prime number")

