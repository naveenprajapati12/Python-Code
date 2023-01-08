n=7
k=7-1
j=0
for i in range(n):
    print("*",end='')
print()
count=0
for i in range(n):
    if j==i or i==k:
        print("*",end='')
    else:
       if count==0: 
         print("Hello",end='')
         count+=1
print()      
for i in range(n):
    if j==i or i==k:
        print("*",end='')
    else:
       if count==1: 
         print("world",end='')
         count+=1
print()      
for i in range(n):
    if j==i or i==k:
        print("*",end='')
    else:
       if count==2: 
         print("in   ",end='')
         count+=1
print()      
for i in range(n):
    if j==i or i==k:
        print("*",end='')
    else:
       if count==3: 
         print("a    ",end='')
         count+=1
print()      
for i in range(n):
    if j==i or i==k:
        print("*",end='')
    else:
       if count==4: 
         print("frame",end='')
         count+=1
       
  
print()
for i in range(n):
    print("*",end='')   
    