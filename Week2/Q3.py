N = 3
matrixA = [[0 for i in range(N)]for j in range(N)]
matrixB = [[0 for i in range(N)]for j in range(N)]
matrixC = [[0 for i in range(N)]for j in range(N)]
number = 1

for i in range(N):
    for j in range(N):
        matrixA[i][j] = number
        number = number + 1
for i in range(N):
    for j in range(N):
        matrixB[i][j] = number
        number = number + 1
        
def Multipilcation(N,MatrixA, MatrixB):
    MatrixC = [[0 for i in range(N)]for j in range(N)]
    for i in range(N):
        for j in range(N):
            Num = 0
            for l in range(N):
                
                Num = Num +(MatrixA [i][l] * MatrixB [l][j])
            MatrixC[i][j] = Num

    print("Multipilcation")
    print("      C1   C2")
    for i in range(N):
            print("R",i+1,"|",MatrixC[i][0],"|" ,MatrixC[i][1])
    print()
            
def Addition(N,MatrixA, MatrixB):
    MatrixC = [[0 for i in range(N)]for j in range(N)]
    for i in range(N):
        for j in range(N):
            MatrixC[i][j] = MatrixA[i][j] + MatrixB[i][j]
    print("Addition")
    print("      C1   C2")
    for i in range(N):
            print("R",i+1,"|",MatrixC[i][0],"|" ,MatrixC[i][1])
    print()

def Subtraction(N,MatrixA, MatrixB):
    MatrixC = [[0 for i in range(N)]for j in range(N)]
    for i in range(N):
        for j in range(N):
            MatrixC[i][j] = MatrixA[i][j] - MatrixB[i][j]
    print("Subtraction")
    print("      C1   C2")
    for i in range(N):
            print("R",i+1,"|",MatrixC[i][0],"|" ,MatrixC[i][1])

Multipilcation(N,matrixA, matrixB)
Addition(N,matrixA, matrixB)
Subtraction(N,matrixA, matrixB)

