from itertools import count

from regex import F


li = list(map(int,input().split()))
n = len(li)
for i in li:
    if li.count(i) >= n//3:
        print(i)
        break

        
   