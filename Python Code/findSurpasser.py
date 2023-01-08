def findSurpasser(arr):
    a=[]
    for i in range(0,len(arr)):
        count=0
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                count+=1
        a.append(count)
    return ' '.join(map(str,a))


n = int(input('Enter size of the array :'))
arr = []
for i in range(n):
    arr.append(int(input()))
print(arr)
print(findSurpasser(arr))