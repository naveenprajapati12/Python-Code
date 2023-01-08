# Given a number N. Count the number of digits in N which evenly divides N.

# Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
 
#  Input:
# N = 12
# Output:
# 2
# Explanation:
# 1, 2 both divide 12 evenly

# Input:
# N = 23
# Output
# 0
# Explanation:
# 2 and 3, none of them
# divide 23 evenly
def countdigits(n):
    temp = n
    count =0
    while temp != 0:
        d= temp % 10
        temp //=10
        if d>0 and n%d==0:
            count+=1
    return count
print(countdigits(int(input())))
        
        