def stringFilter(str1):
    b=''
    for i in str1:
             if "b" in str1:
                    b=str1.replace("b",'')
             if "ac" in str1:
                    c=b.replace("ac",'')
                    
    return c
str1=input()
print(stringFilter(str1))