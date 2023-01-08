n = int(input('How many deletion you wants to perform : '))
list1 = list(map(int,input().split(' ')))
counter = []
for i in list1:
    count = list1.count(i)
    counter.append(count)

counter.sort()
print(counter)
lenght=len(counter)
for i in counter:
    if i <=n:
        n -= count
        lenght-=1
    else:
        break
print(lenght)
