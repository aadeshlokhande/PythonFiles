# ████████████████████ HEAP ████████████████████

# heapify

# [10,5,3,2,4,1]

#             10
#         5       3
#     2       4 1


# child left = 2*i + 1 
# child right = 2*i + 2
# i = 0 ----> 10
#     left = (2*0) + 1 = 1 ---> 5 
#     right = (2*0) + 2 = 2 ---> 3

# i = 1 ---> 5 
#     left = 2*1+1 = 3 ---> 2
#     right = 2*1 +2 = 4 ---> 4 

# i = 2 ----> 3 
#     left ----> 2 * 2 + 1 = 5 ---> 1 

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


def heapify(arr, n, i):
    largest = i #-----> 1 , 3
    left = 2 * i + 1 # ----> 3
    right = 2 * i + 2 # ----> 4

    if left < n and arr[left] > arr[largest]:
        largest = left # ----> 3
    
    if right < n and arr[right] > arr[largest]:
        largest = right 
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, i)
    
def build_heap(arr):
    n = len(arr) # ----> 5
    for i in range(n//2 -1, -1,-1):
        heapify(arr, n, i)

arr = [4,10,3,5,1]
print(arr)

build_heap(arr)
print(arr)

