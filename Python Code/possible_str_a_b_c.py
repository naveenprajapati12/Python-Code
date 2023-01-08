
def countstr(num):
    list = []
    count = 0
    i=0
    a = 0
    b =0
    c =0
    res = 0
    print('You enterd the number is : ',num)
    for l in range(0,num):
        
         if a<=num:
            a+=1
            res += a
         if b<=1:
             b+=1
             res += b
         if c<=2:
             c+=1 
             res += c
         print('a : ',a)
         print('b : ',b)
         print('c : ',c)
         
         for item in range(0,len(list)):
             print(list)
             count += item


        
    return res


num = int(input('Enter the number : '))
res=countstr(num)
print(res)
