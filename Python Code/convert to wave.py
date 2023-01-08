def convertToWave(arr,s):
              
    for i in range(0,s,2):
        if i+1>=s:
            break            
        arr[i],arr[i+1]  = arr[i+1],arr[i]
    print(arr)
    

arr = list(map(int,input().split(',')))
s = len(arr)
arr.sort()
convertToWave(arr,s)