ans_str=" "
str=input("Enter the name with code ")
if str.count(':')!=1:
    print("Wrong input")
else:
    name,code=str.split(':')
    len_name=len(name)
    print("Name length ->",len_name)
    len_code=len(code)
    print("Code length ->",len_code)
    if name.isalpha():
        print(name)
        if code.isdigit():
            print(code)
            max=0
            for i in code:
                if int(i)<= len_code and int(i)>= int(max):
                    max=i
            if max==0:
                ans_str +='X'
            
            else:
                ans_str+=x[int(max)-1]
        print(ans_str)


            
                

            

        else:
            print("invalid input")
    else:
        print("invalid input")