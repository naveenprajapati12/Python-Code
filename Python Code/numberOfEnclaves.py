from itertools import count


def numberOfEnclaves(a,n):
    count=0
    for i in range(n):
        for j in range(1,n-1):
            if a[i][j]==1:
                count+=1
            else:
                continue
    return count
             


n=int(input('Enter the size of the matrix : '))
a=[]
for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input()))
    a.append(b)
print(a)
print(numberOfEnclaves(a,n))

