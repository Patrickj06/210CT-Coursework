
def PerfectN(N,Max,Min):
    '''A function that works out the the highest perfect square number for each number. Done
    by using recusion and binary seac hmethod to find the perfect square number
    paramertes are all integers'''
    Mid = ((Min + Max+1) // 2)  
    if Mid == Max:              #base case - only used if 
         return(Min)            #returns the last perfect square if the midpoint is equal to the max
    Sq = Mid * Mid
    if Sq > N:
        return PerfectN(N,Mid,Min)  
    elif Sq < N:
        return PerfectN(N,Max,Mid)
    else:
        return Mid

Number = int(input("Please input a number :"))

n = PerfectN(Number,Number,1)

if n*n == Number:
    print(Number, "is a perfect square number :" , n, "x", n)
else:
    print(n,"x",n,"=",n*n,"is the closest perfect Square number to", Number)


