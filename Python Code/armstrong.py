x=int(input("Enter the number "))
y=x
z=len(str(x))
j=0
sum=0
while j<z:
    a=x//10
    b=x%10
    sum=sum+b**z
    x=a
    j+=1
if sum==y:
    print("Number {} is armstrong ".format(y))
else:
    print("number {} is not an armstrong".format(y))