def fact(n):
    
    if n==1 :
        return 1
    else:
      fac=1
      for i in range(1,n):
        fac = n * fact(n-1)
    return fac
    
    
arr = list(map(int,input().split(',')))
print(arr)
arr.sort()
print(arr)
res=fact(arr[-1])
print(res)


