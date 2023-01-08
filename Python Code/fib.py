print("Enter the number where you wants to print fibonacci")
x=int(input())
print("\n")
y=0
z=1
temp=2
print(y)
print(z)
while temp!=x:
    val=y+z
    print(val)
    y=z
    z=val
    temp+=1

