def max_min(li):
    max=0
    min=li[0]
for i in li:
    if i>max:
        max=i
    if i<min:
        min=i
        
        return max,min
digits=[12,3,4,5,6,4]
max1,min1 = max_min(digits)
print(max1)
print(min1)