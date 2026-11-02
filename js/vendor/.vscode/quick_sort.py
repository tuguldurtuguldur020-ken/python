# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = [8, 3, 1, 7, 4]
# sorted_numbers = quick_sort(numbers)  
# print(sorted_numbers)
# 1
# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr 

#     pivot = arr[len(arr) // 2 ]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left)+middle+quick_sort(right)

# numbers = [8,3,1,7,0,10,2]
# print(quick_sort(numbers))

# 2
# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr 

#     pivot = arr[len(arr) // 2 ]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num > pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left)+middle+quick_sort(right)

# numbers = [5, 2, 9, 1, 7]
# print(quick_sort(numbers))

# 3
# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr
#     pivot = arr[len(arr) //2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
        
#     return quick_sort(left)+middle+quick_sort(right)
# numbers = [4,2,4,1,2,3,1]
# print(quick_sort(numbers))

# 4
# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr
#     pivot = arr[len(arr) //2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
        
#     return quick_sort(left)+middle+quick_sort(right)
# numbers = [3, -5, 0, 8, -2, 1]
# print(quick_sort(numbers))

# 5
# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr
#     nana = arr[len(arr)//2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < nana:
#             left.append(num)
#         elif num == nana:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left)+middle+quick_sort(right)
# numbers = list(map(int,input("toogoo").split()))
# print(quick_sort(numbers)[0:3])


# 6def quick_sort(arr):
#     if len(arr) <=1:
#         return arr
#     nana = arr[len(arr)//2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < nana:
#             left.append(num)
#         elif num == nana:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left)+middle+quick_sort(right)
# numbers = list(map(int,input("toogoo").split()))
# print(quick_sort(numbers)[:3])


# 7

# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr
#     nana = arr[len(arr)//2]
#     left = []
#     middle = []
#     right = []
#     a = []
#     for num in arr:
#         if num[1]< nana[1]:
#             left.append(num)
#         elif num == nana:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left)+middle+quick_sort(right)
# numbers =  [("Bat", 85), ("Bold", 70), ("Saraa", 95), ("Anu", 60)]
# print(quick_sort(numbers))

# 8
# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr
#     nana = arr[len(arr)//2]
#     left = []
#     middle = []
#     right = []
#     a = []
#     for num in arr:
#         if len(num) < len(nana):
#             left.append(num)
#         elif num == nana:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left)+middle+quick_sort(right)
# numbers =  ["banana", "cat", "apple", "hi", "dog"]
# print(quick_sort(numbers))

# 9
# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr
#     nana = arr[len(arr)//2]
#     left = []
#     middle = []
#     right = []
#     a = []
#     for num in arr:
#         if num < nana:
#             left.append(num)
#         elif num == nana:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left)+middle+quick_sort(right)
# n = len(sort_arr//2)
# numbers =  [7, 1, 5, 3, 9]
# print(quick_sort(numbers))

# 10
def quick_sort(arr):
    if len(arr)<=1:
        return arr
        aa = arr(len(arr)//2)
    left = []
    middle = []
    right = []
    for num in arr:
        if num < aa:
            left.append(arr)
        elif num == aa:
            middle.append(arr)
        else:
            right.append(arr)
    return quick_sort(left)+middle+quick_sort(right)
a = list(map(int,input("toogoo").split()))
b = list(map(int,input("too").split()))
print(quick_sort(a))
print(quick_sort(b))