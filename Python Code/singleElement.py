from gettext import find
from itertools import count
def singleElement(arr):
    counter = []
    res=0
    flag=0
    for i in arr:
        counter.append(arr.count(i))
    #print(counter)
    for j in arr:
         if counter.count(3)==True or counter.count(1)==True:
             flag=1              
             break
                    

    k=1
    if flag==1:
        for i in arr:
            if  arr.count(i)==k:
                res = i
                break

    else:
        print('Wrong input')
    
    return res


N = int(input('Enter the size of the array : '))
arr=[]
for i in range(N): 
    arr.append(int(input()))
print(arr)
Answer = singleElement(arr)
print(Answer)