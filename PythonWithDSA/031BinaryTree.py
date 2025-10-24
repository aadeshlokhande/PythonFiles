# ████████████████████ Binary Search Tree ████████████████████


class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None

def insert(root,data):
    if root==None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root 

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")



"""
Manthan Ka algo
N->Root node,L->Left node,R->right node
preorder->NLR
inorder->LNR
postorder->LRN
"""


bst = None 
bst = insert(bst, 50)
bst = insert(bst, 30)
bst = insert(bst, 70)
bst = insert(bst, 20)
bst = insert(bst, 40)
bst = insert(bst, 60)
bst = insert(bst, 80)

print("\npreorder")
preorder(bst)

print("\ninorder")
inorder(bst)

print("\npostorder")
postorder(bst)

# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛ Homework ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛

# min value 
# max value 
# search element



# class binary_tree:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def insert(root,data):
#     if root==None:
#         return binary_tree(data)
    
#     if data<root.data:
#         root.left=insert(root.left,data)

#     else:
#         root.right=insert(root.right,data)
#     return root

# def preorder(root):  #root->left->right
#     if root:
#         print(root.data,end=" -> ")
#         preorder(root.left)
#         preorder(root.right)
    
# def inorder(root):    # left->root->right
#     if root:
#         inorder(root.left)
#         print(root.data,end=' -> ')
#         inorder(root.right)

# def postorder(root):    #left->right->root
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.data,end=' -> ')




# # bst=None
# # bst=insert(bst,50)
# # bst=insert(bst,30)
# # bst=insert(bst,70)
# # bst=insert(bst,20)
# # bst=insert(bst,40)
# # bst=insert(bst,60)
# # bst=insert(bst,80)

# n=int(input("Enter how many values insert in the BTS: "))
# bst=None
# for i in range(n):
#     val=int(input(f"Enter the value{i+1}: "))
#     bst=insert(bst,val)



# print("\n Inorder Tree")
# inorder(bst)
# print("\n Preorder Tree")
# preorder(bst)
# print("\n Postorder Tree")
# postorder(bst)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ------------------  Find minimum and maximum --------------------

class binary_tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,data):
    if root==None:
        return binary_tree(data)
    
    if data<root.data:
        root.left=insert(root.left,data)

    else:
        root.right=insert(root.right,data)
    return root

def preorder(root):  #root->left->right
    if root:
        print(root.data,end=" -> ")
        preorder(root.left)
        preorder(root.right)
    
def inorder(root):    # left->root->right
    if root:
        inorder(root.left)
        print(root.data,end=' -> ')
        inorder(root.right)

def postorder(root):    #left->right->root
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' -> ')

def min(root):
    current=root
    if current is None:
        return None
    while current.left is not None:
        current=current.left
    return current.data

def max(root):
    current=root
    if current is None:
        return None
    while current.right is not None:
        current=current.right
    return current.data

n=int(input("Enter how many values insert in the BTS: "))
bst=None
for i in range(n):
    val=int(input(f"Enter the value{i+1}: "))
    bst=insert(bst,val)



print("\n Inorder Tree")
inorder(bst)
print("\n Preorder Tree")
preorder(bst)
print("\n Postorder Tree")
postorder(bst)

minimum=min(bst)
print(f"\nThe minimun value of the BST is {minimum}")

maximum=max(bst)
print(f"The maximumvalue in BST is {maximum}")