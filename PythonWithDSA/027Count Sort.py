# ████████████████████ Count Sort ████████████████████


# a = [2,2,3,4,5,5,4,3,5,7,8,9,9,8,7,4,3,4,5,6]
# maxVal = max(a) # 9
# count = [0,0,2,3,4,4,1,2,2,2]
# arr = [2,2,3,3,3,4,4,4,4,5,5,5,5,6,7,7,8,8,9,9]


# def countSort(arr):
#     maxVal = max(arr)
#     # count = [0] * (maxVal+1)
#     count = []
#     for i in range(maxVal+1):
#         count.append(0)
    
#     for i in arr:
#         count[i] += 1

#     sortedArr = []
#     for i in range(len(count)):
#         sortedArr.extend([i] * count[i])

#     return sortedArr
#     # print(count)

# a = [2,2,3,4,5,5,4,3,5,7,8,9,9,8,7,4,3,4,5,6]
# abc = countSort(a)
# print(abc)

# dice = [2,5,1,6,4,2,5,3,4,5,3,2,1,2.......]
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩



# def countSort(arr):
#     count = dict()

#     # for i in arr:
#     #     count[i] = 0

#     for i in arr:
#         try:
#             count[i] = count[i] + 1
#         except:
#             count[i] = 1
    
#     maxVal = max(arr)
#     sortedArr = []
#     minVal = min(arr)
#     for i in range(minVal,maxVal+1):
#         try:
#             sortedArr.extend([i] * count[i])
#         except:
#             pass

#     return sortedArr


# dice = [2,5,1,6,4,2,5,3,4,5,3,2,1,2]
# lol = countSort(dice)
# print(lol)

