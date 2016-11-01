alienNo = [1]

x= int(input("How many eggs does it lay a day :"))
y = int(input("How many days does it take for a egg to hatch :"))

eggs = 0
aliens = 1
for i in range(29):
    
    if i >= 4:
        aliens = aliens + (alienNo[i-y+1] * x)
        eggs = eggs - (alienNo[i-y+1] * 3)
        
    eggs = eggs + (aliens * x)
    'print(aliens * x)'
    alienNo.append(aliens)
    print(eggs)
    
print(alienNo)
