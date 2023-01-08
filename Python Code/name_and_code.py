str=""
str_input=input("Enter word with keys = \n")
a=str_input.split(',')
print(a)
for i in a:
    name,code=i.split(':')
    print(name,code)
    length=len(name)
    max=0
    for j in code:
        if int(j)<=length and int(j)>=int(max):
            max=j
    if max==0:
            str +='X'
    else:
            str=str+name[int(max)-1]
print("result : ",str)
# Anchal:23581,Aman:57568,Sonakshi:34848,Ria:14585