
#Quick Sort
# def pdx(arr, l, h):
#     pivot = arr[h]
#     i = l - 1
#     for j in range(l,h):
#         if arr[j]<= pivot:
#             i+=1
#             arr[j],arr[i] = arr[i],arr[j]
#     i+=1
#     arr[h], arr[i] = arr[i],arr[h]
#     return i
#
# def quickSort(arr, l, h):
#     if l < h:
#         pivot = pdx(arr, l, h)
#         quickSort(arr, l ,pivot-1)
#         quickSort(arr, pivot+1, h)
# arr = [1,3,1,7,23,3]
# quickSort(arr, 0, len(arr) - 1)
# print(arr)

#Merge Sort
# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#         mergeSort(left)
#         mergeSort(right)
#         i= j= k= 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 k+=1
#                 i+=1
#             else:
#                 arr[k] = right[j]
#                 k += 1
#                 j += 1
#         while i < len(left):
#             arr[k] = left[i]
#             k+=1
#             i+=1
#         while j < len(right):
#             arr[k] = right[j]
#             k += 1
#             j += 1
# arr = [7,2,4,6,9]
# mergeSort(arr)
# print(arr)

#kartsuba algorithm for multiplication
# def multiply(x,y):
#     if len(str(x)) < 3 or len(str(y))<3:
#         return x*y
#     n = max(len(str(x)), len(str(y)))//2
#     x1 = x//(10**n)
#     x2 = x%(10**n)
#     y1 = y//(10**n)
#     y2 = y%(10**n)
#
#     F=multiply(x1,y1)
#     G=multiply(x2, y2)
#     H=multiply(x1+x2, y1+y2)
#
#     return F*(10**(n*2))+(H-F-G)*(10**n)+G
#
#
# print(multiply(1000,10000))

