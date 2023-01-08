str=input("Enter the name with code ")
if str.count(':')!=1:
    print("Wrong input")
else:
    name,code=str.split(':')
    if name.isalpha():
        print(name)
        if code.isdigit():
            print(code)
            sum=0
            for i in code:
                sum = sum + int(code[i])**2
            print('The sum is {} '.format(sum))
                
        else:
            print("invalid input")
    else:
            print("invalid input")
    


