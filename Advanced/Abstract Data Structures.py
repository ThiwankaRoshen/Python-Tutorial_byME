# Stack
#list approach
# stack = []
# def push(stack, item):
#     stack.append(item)
# def pop(stack):
#     return stack.pop()
#
# def top(stack):
#     return stack[-1]
#
# def length(stack):
#     return len(stack)
#
# push(stack,45)
# push(stack,45)
# push(stack,45)
# push(stack,45)
# pop(stack)
#
# print(stack)

#class Approach
# class Stack:
#     def __init__(self):
#         self.buffer = []
#         self.length = 0
#     def push(self,item):
#         self.buffer.append(item)
#         self.length+=1
#
#     def pop(self):
#         self.length-=1
#         return self.buffer.pop()
#
#
# stack1 = Stack()
# stack1.push(44)
# stack1.push(44)
# stack1.push(44)
# stack1.pop()
# print(stack1.buffer)


#Queue
#list implementation

# queue = []
#
# def insert(queue, item):
#     queue.append(item)
#
# def remove(queue):
#     return queue.pop(0)
#
# insert(queue, 8)
# insert(queue, 8)
# insert(queue, 8)
# remove(queue)
# print(queue)

#Class implementation
#
# class Queue:
#     def __init__(self):
#         self.buffer = []
#         self.length = 0
#     def insert(self, item):
#         self.buffer.append(item)
#         self.length+=1
#     def remove(self):
#         return self.buffer.pop(0)
#
# q1 = Queue()
# q1.insert(4)
# q1.insert(5)
# q1.remove()
# print(q1.buffer)

#Binary Tree
#List implementation
#i th node
#left of i = 2*i + 1
#right of i = 2*i + 2
# BinaryTree = []
# def addItem(bt, item):
#     bt.append(item)
# def getLeftof(bt, i):
#     return bt[2*i+1]
# def getRightof(bt, i):
#     return bt[2*i+2]

#class implementation

# class BinaryTree:
#     def __init__(self):
#         self.item = None
#         self.left = None
#         self.right = None
#     def preOrder(self):
#         if self.item:
#             print(self.item)
#             if self.left:
#                 self.left.preOrder()
#             if self.right:
#                 self.right.preOrder()
#     def postOrder(self):
#         if self.item:
#             if self.left:
#                 self.left.postOrder()
#             if self.right:
#                 self.right.postOrder()
#             print(self.item)
#     def inOrder(self):
#         if self.item:
#             if self.left:
#                 self.left.inOrder()
#             print(self.item)
#             if self.right:
#                 self.right.inOrder()


# b1 = BinaryTree()
# b1.item = 5
# b1.left = BinaryTree()
# b1.left.item = 4
# b1.right = BinaryTree()
# b1.right.item = 6
# b1.left.left = BinaryTree()
# b1.left.left.item = 3
# b1.left.right = BinaryTree()
# b1.left.right.item = 4.5
# b1.right.left = BinaryTree()
# b1.right.left.item = 5.5
# b1.right.right = BinaryTree()
# b1.right.right.item = 7
#
# # print(b1.left.item, b1.item, b1.right.item)
# b1.inOrder()
