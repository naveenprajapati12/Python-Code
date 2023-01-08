def metaString(s1,s2):
    a=list(s1)
    b=list(s2)
    count = 0
    if len(s1)== len(s2):
        if s1 in s2:
            return 0
        else:
            
            k=0
            n=''
            for i in range(len(s1)):
                if s2[i]==s1[i]:
                    continue
                else:
                    x=b.index(a[i])
                    b[i],b[x]=b[x],b[i] 
                      
            a="".join(b)        
            print("After done swappint",a)
            return 1
                    
            
    else:
        print("Somthing wrong in input ")


S1=input()
S2=input()
print(metaString(S1,S2))