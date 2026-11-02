# numbers = [5, 3, 8, 1, 2]

# n = len(numbers)

# for i in range(n - 1):
#     min_index = i

#     for j in range(i + 1, n):
#         if numbers[j] < numbers[min_index]:
#             min_index = j

#     temp = numbers[i]
#     numbers[i] = numbers[min_index]
#     numbers[min_index] = temp

# print(numbers)



# numbers = [5,3,8,1,2]
# for i in range(len(numbers)-1):
#     min_index = i
#     for j in range(i+1,len(numbers)):
#         if numbers[j] < numbers[min_index]:
#             min_index=j
#     temp = numbers[i]
#     numbers[i] = numbers[min_index]
#     numbers[min_index] = temp 
# print(numbers)




# task1 

# arr = [5,2,8,1,4]
# for i in range(len(arr)-1):
#     min_index = i
#     for o in range(i+1,len(arr)):
#         if arr[o]<arr[min_index]:
#             min_index = o
#     b = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = b
# print(arr)




# task2  
# a = [8,3,6,1,7,2]
# for i in range(len(a)-3):
#     min_index = i
#     for j in range(i+1,len(a)):
#         if a[j]<a[min_index]:
#             min_index=j
#     b = a[i]
#     a[i] = a[min_index]
#     a[min_index]=b
# print(a)


# task3 

# a = [4,9,1,7,3]
# for i in range(len(a)-1):
#     z_index = i
#     for u in range(i+1,len(a)):
#         if a[u]>a[z_index]:
#             z_index = u
#     b =a[i]
#     a[i] = a[z_index]
#     a[z_index]=b
# print(a)


# task 4 

# a = [3,-2,7,-5,1]
# for i in range(len(a)-1):
#     k_index = i
#     for u in range(i+1,len(a)):
#         if a[u] < a[k_index]:
#             k_index=u
#     b = a[i]
#     a[i]=a[k_index]
#     a[k_index]=b
# print(a)

# task5  
# a = [4,2,4,1,2,3]
# for i in range(len(a)-1):
#     min_index = i
#     for p in range(i+1,len(a)):
#         if a[p]<a[min_index]:
#             min_index = p
#     b = a[i]
#     a[i]=a[min_index]
#     a[min_index]=b
# print(set(a))

# task6 
# a = [8,5,3,9,2]
# for i in range((len(a)-1)):
#     min_index = i 
#     for u in range(i+1,len(a)):
#         if a[u]<a[min_index]:
#             min_index = u
#     b = a[i]
#     a[i]=a[min_index]
#     a[min_index]=b
#     break 
# print(a)

# task7 
# a = [8,5,3,9,2]
# for i in range((len(a)-1)):
#     min_index = i 
#     for u in range(i+1,len(a)):
#         if a[u]<a[min_index]:
#             min_index = u
#     b = a[i]
#     a[i]=a[min_index]
#     a[min_index]=b
#     break 
# print(a)

# task8 
# a = [6,3,8,1,5]
# for i in range((len(a)-1)):
#     min_index = i 
#     for u in range(i+1,len(a)):
#         if a[u]<a[min_index]:
#             min_index = u 
#     b = a[i]
#     a[i]=a[min_index]
#     a[min_index]=b
#     break 
# print(a)
# print(a)

# task 9 
# arr = [4, 1, 3, 2]
# count = 0
# for i in range(len(arr)-1):
#     min_index = i 
#     for u in range(i+1,len(arr)):
#         if arr[u]< arr[min_index]:
#             min_index = u 
#     if min_index != i:
#         b = arr[i]
#         arr[i]=arr[min_index]
#         arr[min_index]=b
#         count+=1
# print(count)


# task 10 
# a = [2, 4, 1, 5, 3]
# b = [1, 2, 3, 4, 5]
# c = [3, 1, 2, 5, 4]
# if a == sorted(a):
#     print("a")
# if b == sorted(b):
#     print("b")
# if c == sorted(c):
#     print("c")


# task11 

# def selection_sort(arr):
#     a = len(arr)
#     for i in range(a-1):
#         min_index = i 
#         for u in range(i+1,a):
#             if arr[u] < arr[min_index]:
#                 min_index = u 
#         b = arr[i]
#         arr[i]=arr[min_index]
#         arr[min_index]=b
#     return arr 
# n = list(map(int,input(":").split()))
# print(selection_sort(n))

# task12 
# def selection_sort(arr):
#     a = len(arr)
#     for i in range(a-1):
#         min_index = i 
#         for u in range(i+1,a):
#             if arr[u] > arr[min_index]:
#                 min_index = u 
#         b = arr[i]
#         arr[i]=arr[min_index]
#         arr[min_index]=b
#     return arr 
# n = list(map(int,input(":").split()))
# print(selection_sort(n))

# task13 
# def selection_sort(a):
#     b = len(a)
#     for i in range(b-1):
#         min_index = i 
#         for u in range(i+1,b):
#             if a[u]<a[min_index]:
#                 min_index = u

#         return min_index
# n = list(map(int,input(":").split()))
# print(selection_sort(n))
         

# # task 15 

# arr = [5, 1, 4, 2, 3]
# for i in range(len(arr)-1):
#     for u in range(len(arr)-1-i):
#         if arr[u] < arr[u+1]:
#             b = arr[u]
#             arr[u]=arr[u+1]
#             arr[u+1]=b 
# print(arr) 
def bubble_sort(a):
    for i in range(len(a)-1):
        for u in range(len(a)-1-i):
            if a[i] > a[u+1]:
                b  = a[u+1]
                a[u]=a[u+1]
                a[u+1]=b
n = list(map(int,input().split()))
print(n)
def selection_sort(arr):
    a = len(arr)
    for i in range(a-1):
        min_index = i 
        for u in range(i+1,a):
            if arr[u] > arr[min_index]:
                min_index = u 
        b = arr[i]
        arr[i]=arr[min_index]
        arr[min_index]=b
    return arr 
n = list(map(int,input(":").split()))
print(n)
if selection_sort(n) == bubble_sort(n):
    print("ijil")
else:
    print("ijil bish")