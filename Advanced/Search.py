#Linear Search
# def Search(list, item):
#   """Iterative"""
#     i = 0
#     while i < len(list):
#         if list[i] == item:
#             return i
#         i+=1
#     return -1

# def Search(list, item):
#     """Recursive"""
#     if list[0] == item:
#         return 0
#     if len(list) > 1:
#         return Search(list[1:], item)+1
#     return -100
#
# lis = [99,123,3434,444]
# print(Search(lis, 334))



#Binery Search
# def Search(list, item):
#     """Recursive"""
#     length = len(list)
#     if length == 1:
#         return list[0] == item
#
#     mid = length//2
#     if list[mid] == item:
#         return True
#
#     if len(list) > 1:
#         if list[mid] < item:
#             Search(list[:mid], item)
#         Search(list[mid:], item)



# def Search(list, item):
#     """Iterative"""
#     length = len(list)
#     mid = length//2
#     if list[mid] == item:
#         return True
#     elif list[mid] < item:
#         max = mid
#         min = 0
#     else:
#         max = length-1
#         min = mid
#
#     old = mid
#     mid = (max + min) // 2
#     while old != mid:
#         if item == list[mid]:
#             return True
#         if item < list[mid]:
#             max = mid
#             old = mid
#             mid = (max + min) // 2
#         else:
#             min = mid
#             old = mid
#             mid = (max + min) // 2
#     return False
#
#
# lis = [99,123,3434,444]
# print(Search(lis, 344))



