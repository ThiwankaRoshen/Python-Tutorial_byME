
#Factorial 5! = 1X2X3X4X5
# def fact(n):
#     """Iterative"""
#     if n == 0:
#         return 1
#     else:
#         temp = n
#         while(n>1):
#             temp*=(n-1)
#             n-=1
#     return temp

# def fact(n):
# """Recursive"""
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(5))

#Greatest Common Deviser
# GCD of 10,6 = 2
#10,6
#6, 10%6  = 6, 4
#4, 6%4 = 4,2
#2, 4%2 = 2,0
# def GCD(x,y):
#     """Iterative"""
#     if y == 0:
#         return x
#     else:
#         while y>0:
#             temp = y
#             y = x % y
#             x = temp
#     return x
# def GCD(x,y):
#     """Recursive"""
#     if y==0:
#         return x
#     else:
#         return GCD(y,x%y)
# print(GCD(30,10))
#
# def power(x,n):
#     """Iterative"""
#     if n == 0:
#         return 1
#     else:
#         temp = 1
#         while n>0:
#             temp*=x
#             n-=1
#         return temp

# def power(x,n):
#     """Recursive"""
#     if n==0:
#         return 1
#     else:
#         return x*power(x,n-1)


# def power(x,n):
#     """Recursive + optimized"""
#     if n==0:
#         return 1
#     else:
#         if n%2 == 1:
#             return x*power(x,n//2)*power(x,n//2)
#         return power(x,n//2)*power(x,n//2)

# import time
#
# start_time = time.time()
#
# power(102412312323,17123)//for the recursive only function there is a error called maximum recursive depth
#
# end_time = time.time()
#
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time:.6f} seconds")

#find palindrome
# def isPalindrome(x):
#     leng = len(x)
#     for i in range(1,leng//2 + 1):
#         if x[i] != x[leng-i-1]:
#             return False
#     return True
# def isPalindrome(x):
#     leng = len(x)
#     if leng == 1:
#         return True
#     if leng == 2:
#         return x[0] == x[-1]
#     return (x[0]==x[-1]) and isPalindrome(x[1:-1])
# print(isPalindrome("HelleH"))

#Tower of Hanoi
# def steps(n, fro, to, spare):
#     if n == 1:
#         print(f"{1} from {fro} to {to}")
#         return
#     steps(n-1, fro, spare, to)
#     print(f"{n} from {fro} to {to}")
#     steps(n-1, spare, to, fro)
# steps(3,'A','B','C')