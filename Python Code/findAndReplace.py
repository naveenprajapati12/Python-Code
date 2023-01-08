def findAndreplace(S,Q,index,sources,targets):
    ans = ''
    space = 0
    for i in range(Q):
                       
      ans = ans + S[len(ans) - space :  index[i]]
     
      if S[index[i] : index[i] + len(sources[i])] == sources[i] :
       
        space += len(targets[i]) - len(sources[i])
       
        ans += targets[i]
    ans += S[len(ans) - space :]
   
    return ans
 
            


S = input('Enter string : ')
Q = int(input('how many replace operation you want to perform : '))
index = []
sources = []
targets=[]
res=''
if 1<= Q <= 100: 
    for i in range(Q):
      index.append(int(input()))
    print('index : ',index)

    for i in range(Q):
      sources.append(input())
    print('sources : ',sources)

    for i in range(Q):
       targets.append(input())
    print('targets : ',targets)
    
    print(findAndreplace(S,Q,index,sources,targets))       
else:
    print('out of range ')