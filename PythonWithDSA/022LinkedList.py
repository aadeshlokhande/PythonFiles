# ████████████████████ Linked List ████████████████████


# list = [12,32,54,76,87]
# list.insert(1,10)
# list = [12,10,32,54,76,87,.........]


# ████████████████████ singular linked list ████████████████████


# NODE creation
# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)

# node1.next = node2
# node2.next = node5
# node3.next = node4
# node5.next = node3

# current = node1

# while current is not None:
#     print(current.data, end = " ===> ")
#     current = current.next
# print("None")


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# class Node:
#     def __init__(self, data):
#         self.data = data 
#         self.next = None 



# class SingleLL:
#     def __init__(self):
#         self.head = None 
    
#     def insert(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node
        
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" ===> ")
#             current = current.next
#         print("None")
# 10 ---> 20 ---> 30 ---> 40 ----> 50

# linkedList = SingleLL()
# linkedList.insert(11)
# linkedList.insert(22)
# linkedList.insert(33)
# linkedList.insert(44)
# linkedList.insert(55)
# linkedList.insert(66)
# linkedList.insert(77)
# linkedList.display()


# ll = SingleLL()
# num = int(input("kitne values store krne hai = "))
# for i in range(num):
#     value = int(input("enter a number = "))
#     ll.insert(value)

# ll.display()

    
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None 
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2
# node2.next = node3
# node3.prev = node2
# node2.prev = node1



# print("Forward --> ",end="")
# current = node1
# while current:
#     print(current.data, end=" <==> ")
#     current = current.next 
# print("None")

# print("Backward --> ",end="")
# current = node3
# while current:
#     print(current.data, end=" <===> ")
#     current = current.prev
# print("None")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# a = "eat" #:-----> a,e,t 
# b = "ate" #:-----> a,e,t 
# a = sorted(a)
# b = sorted(b)
# if(a==b):
#     print("Anagram")



# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# a = "aadesh"
# b = "swarnim"
# a = list(a)
# b = list(b)

# lst  = []
# for ch in a:
#     if(ch in b):
#         b.remove(ch)
#         lst.append(ch)

# if(len(a) == len(lst)):
#     print("hai")

# print(lst)
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩




