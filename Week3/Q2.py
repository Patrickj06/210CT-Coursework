
def primeNumber(n,test):
    if test == 1:
        return True
    if n % (test) == 0:
        return False
    elif n % (test) != 0:
        return primeNumber(n,test+1)

number = int(input("Please enter number :"))
output = primeNumber(number,2)

if output == False:
    print(number, " is not a prime number")
else:
    print(number, "is a prime number")

