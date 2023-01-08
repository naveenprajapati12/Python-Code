number=int(input("Enter number which you wants to check prime or not  "))
if number>1:
    for i in range(2,number):
        if(number%i)==0:
            print("Number {} is not a prime number".format(number))
            break
    else:
        print("Number {} is prime number ".format(number))
