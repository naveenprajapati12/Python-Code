x=input("Enter the number ")
y=len(x)
first=0
last=y-1
flag=0
while 1:
    if x[first]==x[last]:
        if first==last or last<first:
            break
        else:
            first+=1
            last-=1
    else:
        flag=1
        break
 
if flag==0:
    print("Number {} is palindrom ".format(x))
else:
    print("Number {} is NOT palindrom ".format(x))

             
    