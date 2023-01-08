str = input('Enter the string : ')
p = ''
for char in str:
    if char not in p:
        p=p+char
print(p)

p = p[::-1]
print(p)
