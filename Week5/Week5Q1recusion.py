Array = [0,1,2,6,3,1,4,5,6,7]
def maxLengthInOrder(nArray):
    '''Function that counts the largest ascending sequence inside a list 
    '''
    longArray = [0,0]                           # array for pointers of max list 
    p1 = 0                                      # start of current list
    
    for i in range(len(nArray)-1):
        if nArray[i+1] < nArray[i]:             #Checks for increase 
            if (i - p1) >= (longArray[1] - longArray[0]):                
                longArray = [p1,i]              #Checks the difference of two lists
            p1 = i + 1
            
    if (i - p1) >= (longArray[1] - longArray[0]): 
        longArray = [p1,i+1]
        
    return nArray[longArray[0]:longArray[1]+1] 

print(maxLengthInOrder(Array))  
