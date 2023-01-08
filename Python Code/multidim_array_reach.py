list1 = []
list2=[]
list = []
n = int(input('Enter the size of an array : '))
for i in range(n):
    list1.append(input())
for i in range(n):
    list2.append(input())

list.append(list1)
list.append(list2)
print(list)
res=[]
for i in range(n):
    sum = 0
    for j in range(n):
        sum = sum+int(list[i][j])
    res.append(sum)

res.sort()   
print(res[-1])


