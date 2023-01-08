'''
Number of odd sub arrays. Find the number of distinct subarrays in an array of position integers such that the sum of the subarray is an odd integer, two subarrays are considered different if they either start or end at different index.

Input:
3
1 2 3
Output:4

1 
1 2 
1 2 3 
2 
2 3 
3 
'''
n=int(input())
arr = []
for i in range(n):
    val = int(input())
    arr.append(val)
print()
count=0
for i in range(n):
    sum=0
    for j in range(i,n):
        for k in range(i,j+1):
            print(arr[k],end=' ')
            sum=sum+arr[k]  
            if sum%2==0:
                  break
            else:
                count+=1
        print()

print("\n The Answer is : ")
print(count)
  

    