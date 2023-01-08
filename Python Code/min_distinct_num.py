x=int(input('Enter deletion number as you want : '))
li=list(map(int,input().split(' ')))
c=[li.count(i) for i in li]
c.sort()
k=0
if k<x:
   for i in c:
      c.remove(i)
      k+=0

print(max(c))
    