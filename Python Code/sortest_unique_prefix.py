def findPrefix(arr,n):
    y=[]
    counter = []
    k=' '.join(arr)
    length =len(k)
    k1=' '.join(y)
    print(k)
    for i in arr:
       for j in k:
           if arr[i]==j:
               y.append(j)
           else:
                y.append(j)
        
        

            
    print(y)        
    
    return k1

x = int(input('Enter the number : '))
arr=[]
for i in range(x):
    arr.append(input())
print(arr)

res = findPrefix(arr,x)
print(res)