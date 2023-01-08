s1 = input('Enter data for s1 : ')
a = len(s1)
s2 = input('Enter data for s2 : ')
b = len(s2)
count=0
sum=0
if s1.isalpha() == True and s2.isalpha() == True:
    for i in range(0,b):
        for j in range(0,a):
            if s2[i] == s1[j]:
                count -= j
                c=abs(count)
                count = c
                sum += count
            else:
                pass
else:
    print('Something wrong in the input')

print(sum)