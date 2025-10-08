# ████████████████████ Merge Sort ████████████████████


# a = [23,43,12,76,54,32,58,21,23,97,23,10]
# len(a)//2 = 6

# 23,43,12,76,54,32           58,21,23,97,23,10
# 23,43,12,       76,54,32           58,21,23,        97,23,10
# 23,     43,12,       76,        54,32           58,     21,23,        97,       23,10
# 23,     43,     12,       76,        54,        32           58,     21,        23,        97,       23,        10
# 23,43       12,76       32,54       21,58       23,97       10,23
# 12,23,43,76         21,32,54,58         10,23,23,97

# 12,21,23,43,54,58,76            10,23,23,45
# i<j

# new = []
# new.append(10)
# new.append(12)
# new.append(21)
# new.append(23)
# new.append(23)
# new.append(23)
# new.append(43)
# new.append(45)
# .
# .
# .
# .
# new.extend(b[j:])
# new.extend(b[i:])




# def merge(left, right):
#     new = []
#     i = 0
#     j = 0

#     while i<len(left) and j<len(right):
#         if left[i] < right[j]:
#             new.append(left[i])
#             i += 1
#         else:
#             new.append(right[j])
#             j += 1
    
#     new.extend(left[i:])
#     new.extend(right[j:])
#     return new


# def mergeSort(arr):
#     if len(arr) <=1:
#         return arr
#     mid = len(arr) // 2
#     l_half = arr[:mid]
#     r_half = arr[mid:]

#     l_half = mergeSort(l_half)
#     r_half = mergeSort(r_half)

#     return merge(l_half,r_half)


# a = [23,43,12,76,54,32,58,21,23,97,23,10]
# print(a)
# # lol = mergeSort(a)
# # print(lol)

# lol = mergeSort(a)
# print(a)
# print(lol)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩




# ████████████████████ Vivan Code ████████████████████
# def merge(arr,n,low,mid,high):
#     temp=[0 for _ in range(n)]
#     i=low
#     j=mid+1
#     k=0
#     while i<=mid and j<=high:
#         if arr[i]<=arr[j]:
#             temp[k]=arr[i]
#             i+=1
#         else:
#             temp[k]=arr[j]
#             j+=1
#         k+=1
    
#     if i<=low:
#         while i<=low:
#             temp[k]=arr[i]
#             i+=1
#             k+=1
#     if j<=high:
#         while j<=high:
#             temp[k]=arr[j]
#             j+=1
#             k+=1
#     k=0
#     for i in range(low,high+1):
#         arr[i]=temp[k]
#         k+=1


# def merge_sort(arr,n,low,high):
#     if low<high:
#         mid=(low+high)//2
#         merge_sort(arr,n,low,mid)
#         merge_sort(arr,n,mid+1,high)
#         merge(arr,n,low,mid,high)

# n=int(input("enter number of elements: "))
# arr=[0 for _ in range(n)]

# for i in range(n):
#     arr[i]=int(input(f"enter element arr[{i}]: "))

# print("elements before sorting")
# for i in range(n):
#     print(f"element arr[{i}]: {arr[i]}")

# merge_sort(arr,n,0,n-1)

# print(arr)

