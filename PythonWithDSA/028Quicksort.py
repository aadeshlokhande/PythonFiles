# ████████████████████ Quick Sort ████████████████████


def partition(arr,low, high):
    p = arr[low]
    i = low + 1
    j = high
    while True:
        while i<=j and p>=arr[i]:
            i += 1
        while i<=j and p<=arr[j]:
            j-=1
        if i<=j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low],arr[j] = arr[j], arr[low]
    return j 

def quickSort(arr, low, high):
    if low<high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr,pivot+1 ,high)
a = [5,8,1,2,6,3,9]
# a = [3,1,2,5,6,8,9]
print(a)
quickSort(a,0,len(a)-1)
print(a)
