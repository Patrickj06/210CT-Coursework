
def binarySearch(L,low,high):
    Min = 0
    Max = len(L)-1
    done = False 
    while done != True:
        Mid = (Min + Max) // 2
        if Mid == Min:
            return False
        
        if (L[Mid] >= low) and (L[Mid] <= high):
            return True
        else :
            if L[Mid] < low:
                Min = Mid
            else:
                Max = Mid
        
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
