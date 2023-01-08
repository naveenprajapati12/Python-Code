a=int(input("Enter starting num "))
b=int(input("Enter ending num "))
print("prime number between {} and {} ".format(a,b))
for number in range(a,b+1):
    if 1<number:
        for i in range(2,number):
            if(number%i)==0:
                break
   
        else:
         print(number)

    
