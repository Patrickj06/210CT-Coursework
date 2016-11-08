
def binarySearch(L,low,high):
    if len(L) <1:
        return False
    mid = (1 + len(L)) // 2 - 1
    if (L[mid] >= low) and (L[mid] <= high):
        return True
    else:
        if L[mid] < low:
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
