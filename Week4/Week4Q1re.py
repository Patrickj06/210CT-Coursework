
def binarySearch(L,low,high):
    '''Recusive adaped binary search algorithm that returns true or
    false if there is a number in the range of lower and upper bound
    Parameters: L is a list, low and high are integers
    '''
    if len(L) <1:                            #Base case if the length of the list is 
        return False                         #empty then it hasn't found it in the range      
    mid = (1 + len(L)) // 2 - 1
    if (L[mid] >= low) and (L[mid] <= high): #If in range then return true
        return True
    else:
        if L[mid] < low:                     #If mid lower that lower bound then cut list at mid
            return binarySearch(L[mid+1:],low,high)
        else:                               
            return binarySearch(L[:mid],low,high)

Array = [11,26,37,51,64,79,96,109,134,152]
print(Array)
done = False

while done != True:
    Low = int(input("Please input the lower bound :"))
    High = int(input("Please input the upper bound :"))
    if High >= Low:
        done = True
    else:
        print("ERROR-Enter a lower number than the high bound")
        print()
        
print(binarySearch(Array,Low,High))
