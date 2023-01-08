n = int(input('Enter the matrix n*n : '))
matrix = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)
print(matrix)
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end= ' ')
    print()
print()      
for i in range(n-1,-1,-1):
    for j in range(0,n,1):
        print(matrix[j][i], end= ' ')
    print()
        

        
