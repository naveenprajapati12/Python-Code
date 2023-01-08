str = int(input())
list_num=list(map(int,input().split(" ")))
list_count = []
unique = set(list_num)
for i in unique:
    count = list_num.count(i)
    list_count.append(count)
list_count.sort()
length=len(list_count)
for count in list_count:
    if count<=str:
        str-=count
        length -=1
    else:
        break
print(length)  
    



