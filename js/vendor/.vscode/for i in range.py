# for i in range(5):

#     print("sainuu")

# 2

# for i in range(0,10):
#     print(i)

# 3

# for i in range(1,11):
#     print(i)

# 4

# for i in range(10,0,-1):

#     print(i,end=" ")

# 5

# for i in range(5):

#     print("tuguldur")

# 6
# total = 0

# for i in range(1,11):

#     total+=i
# print(total)

# 7
# total = 0 

# for i in range(1, 101):

#     total+=i
# print(total)

# 8
# total = 0 

# for i in range(1,21):

#     if i%2==0:

#         total+=i
#     print(total)    

# 9
# total = 0 

# for i in range(1,31):

#     if i %3==0:

#         total+=i
#         print(total)
# 10

# n = int(input(":"))
# total = 0 

# for i in range(n+1):

#     total+=i
# print(total)
# 11

# count = 0 

# for i in range(1,21):

#     if i % 2 == 0:

#         count+=1

# print(count)

# 12

# count = 0 

# for i in range(1,101):

#     if i % 5 == 0:

#         count+=1

#         print(count)

# 13

# count = 0 

# for i in range(1,51):

#     if i % 3 ==0:

#         count+=1

#         print(count)

# 14

# tegsh = 0 

# sondgoi = 0 

# for i in range(1,21):

#     if i % 2 ==0:

#         tegsh+=1

#     else:

#         sondgoi+=1

# print(f"tegsh too bn:{tegsh}")

# print(f"sondgoi too bn:{sondgoi}")

# # print(tegsh,"tegsh too")

# print(sondgoi,"sondgoi too")

# 15
# n = int(input(":"))

# count = 0 

# for i in range(1,n+1):

#     if i % 7 ==0:

#         count+=1

# print(count)

# 16
# total = 0 

# count = 0 

# for i in range(1,101,+1):

#     if i % 2 == 0:

#         total+=i

#         count+=1
# print(total)

# print(count)

# 17

# count=0

# for i in range(1,101):

#     if i % 3 ==0 or i % 5 ==0:

#         count+=1

# print(count)

# # 18
# total = 0

# for i in range(1,101):

#     if i % 3 ==0:

#         total+=i
#         print(total)

# 19################################

# a = int(input("suragchidaa"))
# total = 0 

# count = 0 
# for i in range(a):
#     onoo = int(input(":"))

#     total+=onoo

#     if onoo >80:

#         count+=1
        

# c = total / a

# print("niilber",total)

# print("dundaj",c)

# print("80aasdeesh",count)

# 20

# n = int(input("heden den oruulah ve"))

# best = 0 
# for i in range(n):

#     dun = int(input())

#     if dun > best:

#         best=dun

# print(f"hamgiin ondor dun",best)

# # 21

# n = int(input(";;"))

# hamgiin_baga = int(input("hed ve"))
# for i in range(n):

#     dun = int(input())

#     if dun < hamgiin_baga:

#         hamgiin_baga = dun

# print(f"hamgiin baga dun",hamgiin_baga)

# 22
# n = input()

# s = 0

# for i in n:

#     s += int(i)


# print(s)
# 23
# n = int(input(":"))
# result = 1 
# for i in range(1,n+1):
#     result*=i
# print(result)
# 24
# n = int(input(":"))
# total = 0
# for i in range(1,n):
#     if n % i ==0:
#         total+=i
# if total ==n:
#     print("yes")
# else:
#     print("no")
# 25
# n = int(input())
# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1

# if count == 2:
#     print("YES")
# else:
#     print("NO")
# n = int(input())
# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count = count + 1

# if count == 2:
#     print("YES")
# else:
#     print("NO")

count = 0 
for i in range(1,101):
    if i % 2 ==0 or i % 3 ==0 or i % 5==0:
        count+=1
print(count)