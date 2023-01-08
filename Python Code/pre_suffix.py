s=input('Enter the string : ')
j = len(s)
count=0
mid = j//2
for i in range(mid):
    if s[i]==s[mid+1]:
        count+=1
        i+=1
        mid+=1
        
print(count)
    
