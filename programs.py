#prime number


# def isprime(n):
#
#         for i in range(2,n):
#             if n%i==0:
#                 print("not prime")
#                 break
#         else:
#            print("prime")
#
# n = int(input("enter a number : "))
# isprime(n)



#prime number range


def prime_range(n1,n2):
    for i in range(n1,n2+1):
        for j in range(2,i):
            if i%j == 0:
                # print("not prime")
                break
        else:
            print("prime,",i)

lower_num = int(input("enter the lower limit num : "))
upper_num = int(input("enter the upper limit num : "))

prime_range(lower_num,upper_num)