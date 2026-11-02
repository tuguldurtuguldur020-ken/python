# TASK1 
# i = int(input(":"))
# if i % 2==0:
#         print(" eyreg_tegsh")
# else:
#         print(" sorog_sondgoi")


# TASK 2
# a = int(input("onoogoo"))
# if a > 100:
#     print("buruu too")
# elif a >= 90:
#     print("A")
# elif a >= 80:
#     print("B")
# elif a >= 70:
#     print("C")
# elif a >= 60:
#     print("D")
# else:
#     print("F")

# TASK 3

# a = int(input("jilee oruul: "))

# if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
#     print("ondor jil ")
# else:
#     print("engiin")


# TASK 4

# a = int(input("a talaa oruul : "))
# b = int(input("b talaa oruul : "))
# c = int(input("c talaa oruul : "))
# if a + b <= c or a + c <=b or b + c <=a:
#     print("gurvaljin uusehguii")
# elif a == b == c:
#     print("tegsh talt")
# elif a == b or a == c or b == c:
#     print("adil hajuut")
# else:
#     print("engiin")


# TASK 5 
# a = int(input("heden km yvsan be ? :"))
# b = int(input("heden tsagt yvsan be ? : "))
# if a <2:
#     print("3000")
# # elif a>=2:
# #     print("1500")
# if b > 22:
#     print("shoniin tolbor")


# task 6 
# a = int(input(":"))
# count = 0 
# for i in range(1,a+1):
#     if i % 2 ==0:
#         count+=i
# print(count)

# task 7
# n = int(input("too : "))
# t= 0 
# while n > 0:
#     b = n % 10
#     t+=b
#     n = n //10
# print(t)

# task8
# n = int(input(":"))
# a = []
# niit = 0 
# while n > 0:
#     b = n % 10
#     a.append(b)
#     n = n //10
# for i in a:
#     niit = niit * 10 + i 
# print(niit)


# 10

# too = 25
# count = 0 
# while count < 5:
#     b = int(input("toogoo taa : "))
#     count+=1
    
#     if b > too:
#         print("ih bn")
#     elif b < too:
#         print("baga bn")
#     else:
#         print(f"zov {count} oroldlogoor taalaa ")
#         break 
# if b != too and count == 5:
#     print("hojilgdloo")

# 11
# n =  int(input("n:"))
# for i in range(1, n + 1):
#     for u in range(1, n + 1):
#         print(i * u, end=" ")
#     print()
# n = int(input("n: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end=" ")
#     print()

# 12

n = int(input())
for i in range(1, n + 1):
    for u in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="") 
    print()
# 13
# def find_pairs(arr, target):
#     result = []
#     for i in arr:
#         for j in arr:
#             if i < j:
#                 if i + j == target:
#                     result.append(i)
#                     result.append(j)
#                     print(result)
#                     result = []

# find_pairs([2,7,4,5,1], 6)