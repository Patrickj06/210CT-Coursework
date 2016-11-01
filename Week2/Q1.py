
def PerfectN(N,Max,Min):
    Mid = ((Min + Max+1) // 2)
    if Mid == Max:
         return(Min) #returns the last perfect square if the midpoint is equal to the max
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


