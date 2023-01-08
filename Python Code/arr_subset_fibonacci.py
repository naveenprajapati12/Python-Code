
def findFibSubset(arr,n):
    m = max(arr)
    a=0
    b=1
    fib=[]
    # fib.append(a)
    # fib.append(b)
    while (b<m):
        count =0
        c = a+b
        a=b
        b=c
        fib.append(b)
    
    for i in range(n):
           if arr[i] in fib:
               count+=1
    if 2<count:
      print(count,end="([ ")
      for i in range(n):
        if arr[i] in fib:
          print( arr[i],end=" ")
      print('',end='])')
    else:
        print('-1')      
         

print('Enter element with comma seperated : \n')
list_num = list(map(int,input().split(',')))
n = len(list_num)
findFibSubset(list_num,n)