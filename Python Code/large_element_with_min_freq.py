T = int(input('Enter the size : '))
arr=[]

for i in range(T):
    a = int(input())
    arr.append(a)
counts = []
print()    
print(arr)

for i in arr:
    counts.append(arr.count(i))
m = min(counts)
arr.sort()
arr.reverse()
for i in arr:
     if arr.count(i) == m: # if arr's data count is equal to min count of counts[] to that print max
         print(i)
         break


    



