# nums = list(map(int, input("Toonuud :").split()))


# for i in range(len(nums) -1):


#     for j in range(len(nums)-1 -i):


#         if nums[j] > nums[j+1]:


#             a = nums[j]


#             nums[j] = nums[j+1]


#             nums[j+1]=a


# print(nums)





# task2



# a = list(map(int,input("toogooo og : ").split()))


# for i in range(len(a) - 1): 


#     for o in range(len(a) - 1 - i): 


#         if a[o] < a[o+1]:


#             b = a[o]

#             a[o] = a[o+1] 


#             a[o+1]=b
# print(a)



# task3



# a = list(map(int,input(":").split()))


# for i in range(len(a) - 1):


#     for y in range(len(a) - 1 - i):


#         if a[y] > a[y+1]:


#             b = a[y]


#             a[y] = a[y+1]


#             a[y+1]=b
# print(a)




# task4



# a = list(map(int,input(":").split()))


# for i in range(len(a) - 1 ):


#     for  u in range(len(a) - 1 - i):


#         if a[u] > a[u+1]:


#             b = a[u]

#             a[u] = a[u+1]


#             a[u+1]=b
# print(a)





# # task5


# a = list(map(int,input(":").split()))


# for i in range(len(a) - 1):


#     for k in range(len(a) - 1 - i):


#         if a[k] > a[k+1]:


#             b = a[k]


#             a[k] = a[k+1]


#             a[k+1]=b
# print(a)




# TASK6



# a = list(map(str,input(":").split()))


# for i in range(len(a) - 1):


#     for p in range(len(a) -1 -i):


#         if a[p] > a[p+1]:


#             b = a[p]

#             a[p] = a[p+1]


#             a[p+1]=b
# print(a)



# # task7


# a = list(map(int,input("scores").split()))


# for i in range(len(a)-1):


#     for k in range(len(a)-1-i):


#         if a[k] > a[k+1]:


#             b = a[k]


#             a[k] = a[k+1]


#             a[k+1]=b
# print(a)




# task8



# a = list(map(int,input(":").split()))


# for i in range(len(a)-1):


#     if a[i] >= a[i+1]:


#         b = a[i]

#         a[i] = a[i+1]


#         a[i+1]=b
# print(a)



# task9


# a = list(map(int,input(":").split()))


# count = 0


# for i in range(len(a)-1):


#     count+=1


#     for u in range(len(a)-1-i):


#         if a[u] > a[u+1]:


#             b = a[u]

#             a[u]=a[u+1]


#             a[u+1]=b


# print(a,count)




# task10



# a = list(map(int,input(":").split()))


# count = 0 


# for i in range(len(a)-1):


#     for t in range(len(a)-1-i):


#         count+=1


#         if a[t] > a[t+1]:


#             b = a[t]

#             a[t]=a[t+1]


#             a[t+1]=b


# print(a,count)



# task11



# a = list(map(int,input(":").split()))


# for i in range(len(a)-1):


#     for p in range(len(a)-1-i):


#         if a[p] <=a[p+1]:


#             b = a[p]

#             a[p]=a[p+1]


#             a[p+1]=b
# print(a[1])



# task12



# a = list(map(int,input(":").split()))


# for i in range(len(a)-1):


#     for o in range(len(a)-1-i):


#         if a[o]> a[o+1]:


#             b = a[o]

#             a[o]=a[o+1]


#             a[o+1]=b
# print(a)




# task13



# a = list(map(int,input(":").split()))


# for i in range(len(a)-1):


#     for o in range(len(a)-1-i):


#         if a[o]>=a[o+1]:


#             b = a[o]

#             a[o]=a[+1]


#             a[o+1]=b
#             print(a)




# task14



# a = list(map(int,input(":").split()))


# for i in range(len(a)-1):


#     for u in range(len(a)-1-i):


#         if a[u]>a[u+1]:


#             b = a[u]

#             a[u]=a[u+1]


#             a[u+1]=b
# print(a)  #############################      

#    1-р арга — a нь list байх үед:1-р арга — a нь list байх үед:

# for i in range(len(a) - 1):

#     for u in range(len(a) - 1 - i):
#         print(u)


# task15




# a = list(map(int,input(":").split()))


# c = 0


# swapped = False


# for i in range(len(a)-1):


#     c+=1


#     for u in range(len(a)-1-i):
        


#         if a[u]>a[u+1]:


#             b = a[u]

#             a[u]=a[u+1]


#             a[u+1]=b


#             swapped = True
#         else:


#             swapped = False


#     if swapped == False:


#         print(a,c)


#         break
            




# task16
######################################


# students = [


#     ["Bat", 75],


#     ["Saraa", 92],


#     ["Anu", 60],


#     ["Bold", 88]
# ]

# a = len(students)


# for i in range(len(students)-1):


#     for u in range(len(students)-1-i):

#         if students[u]>=students[u+1]:


#             b =students[u]

#             students[u]=students[u+1]

#             students[u+1]=b

# for i in range(a):

#         print(f"{students[i][1]},{students[i][1]}",end = " ")



# task17


# people = [

#     ["Bat", 19],

#     ["Anu", 17],

#     ["Bold", 21],

#     ["Saraa", 18]
# ]
# o =len(people)

# for i in range(o - 1):

#     for m in range(o - 1 - i):

#         if people[m][1]>=people[m+1][1]:

#             b = people[m]

#             people[m]=people[m+1]

#             people[m+1]=b
# print(people)


#################
# task18
# a нь элементийн тоо байх үед:
# a = len(people)


# for i in range(a - 1):

#     for u in range(a - 1 - i):
#         print(u)


# # # task######################
# numbers = [4, 2, 4, 1, 2, 4,]
# a = len(numbers)
# for i in range(a-1):
#     for u in range(a-1-i):
#         if numbers[i] > numbers[u+1]:
#             b = numbers[u]
#             numbers [u] == numbers[u+1]
#             numbers[u+1]
# count
# for i in range(len(numbers)-1):
#     if  numbers[i]==numbers[i+1]:
#         count+=1
# print(numbers)
# print(count)


# task19

# task19

# people = [
#     ["Mouse", 25000],
#     ["Keyboard", 65000],
#     ["USB", 12000],
#     ["Headphone", 80000]
# ]

# o =len(people)
# for i in range(o - 1):
#     for m in range(o - 1 - i):
#         if people[m][1]<=people[m+1][1]:
#             b = people[m]
#             people[m]=people[m+1]
#             people[m+1]=b
# print(people[:3]) 



# n = list(map(int,input(":").split()))
# count = 0 
# x = 0
# z = 0 
# for i in range(len(n)-1):
#     count+=1
#     for u in range(len(n)-1-i):
#         x+=1
#         if n[u]>n[u+1]:
#             b = n[u]
#             n[u]=n[u+1]
#             n[u+1]=b
#             z+=1
# print(f"gadna davtalt : {count}\nsoliltsoo : {x}\nniit haritsuulalt: {z}")






# 21
# n = list(map(int,input(":").split()))
# for i in range(len(n)-1):
#     for u in  range(len(n)-1-i):
#         if n[u]>n[u+1]:
#             b = n[u]
#             n[u]=n[u+1]
#             n[u+1]=b
# print(n,b)

# 22

# b  = list(map(str,input(":").split()))
# for i in range(len(b)):
#     for u in range(len(b)-1-i):
#         if len(b[u])>len(b[u+1]):
#             n = b[u]
#             b[u]=b[u+1]
#             b[u+1]=n
# print(b)



# 23


# n  = list(map(int,input(":").split()))
# for i in range(len(n)-1, 0, -1 ):
#     if n[i]<n[i-1]:
#         n[i],n[i-1] = n[i-1],n[i]
# print(n)

# 24

# a = list(map(int,input(":").split()))
# for i in range(len(a)-1):
#     for o in range(len(a)-1-i):
#         if a[o] %2==1 and a[o+1]%2==0:
#                 a[o], a[o+1] = a[o+1],a[o]
# print(a)

