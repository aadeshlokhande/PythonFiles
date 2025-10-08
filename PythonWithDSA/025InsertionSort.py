# ████████████████████ Insertion Sort ████████████████████
# data set = 4,1,2,5,6,3

# 4 
# 3 4 
# 1  2   3   4   5   6
# 1 2 3  4   5   6




def insertionSort(nums):
    n = len(nums)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1 
        arr[j+1] = key

arr = [35,40,30,20,10]
insertionSort(arr)

print(arr)


# key = 25
# 10,20,25,30,40,50