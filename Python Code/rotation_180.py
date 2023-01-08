n = int(input('Enter the size row and colom '))
mat= []
for i in range(n):
    y=[]
    for j in range(n):
        y.append(input())
    mat.append(y)
print(mat)
for i in range(n):
    for j in range(n):
        print(mat[i][j],end=' ')
    print()

print()
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        print(mat[i][j],end=' ')
    print()
        
