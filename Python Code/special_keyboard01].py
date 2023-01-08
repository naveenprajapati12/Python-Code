s1 = input('Enter data for s1 : ')
s2 = input('Enter data for s2 : ')
count=0
sum=0
if s1.isalpha() == True and s2.isalpha() == True:
    for j in s2:
        k=s1.index(j)
        count -= k
        a=abs(count)
        count = a
        sum += count
else:
    print('Something Wrong in input ')
print(sum)
