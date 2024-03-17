#Bubble Sort
# def sort(list):
#     length = len(list)
#     for i in range(length):
#         for j in range(length-1):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]

#Selection Sort
# def sort(list):
#     length = len(list)
#     for i in range(length):
#         max = list[0]
#         idx = 0
#         for j in range(length -i):
#             if max < list[j]:
#                 max=list[j]
#                 idx = j
#         list[length -i-1], list[idx] = list[idx], list[length -i-1]


#insertion Sort
# def sort(list):
#     for id in range(1, len(list)):
#         current = list[id]
#         pos = id
#
#         while pos>0 and current<list[pos-1]:
#             list[pos] = list[pos -1]
#             pos-=1
#
#         list[pos] = current
#
#
# lis = [4,1,2,7,3]
# sort(lis)
# print(lis)


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


# def shell_sort(a_list):
#     sublist_count = len(a_list) // 2
#
#     while sublist_count > 0:
#         for start_pos in range(sublist_count):
#             gap_insertion_sort(a_list,start_pos,sublist_count)
#
#         sublist_count = sublist_count // 2
#
# def gap_insertion_sort(a_list, start, gap):
#     for i in range(start + gap, len(a_list), gap):
#         current_value = a_list[i]
#         pos = i
#
#         while pos >= gap and a_list[pos-gap] > current_value:
#             a_list[pos] = a_list[pos - gap]
#             pos = pos - gap
#
#         a_list[pos] = current_value
#
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# shell_sort(a_list)
# print(a_list)


# To heapify subtree rooted at index i. Heap size is n.
def heapify(a_list, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1 # left = 2*i + 1
    r = 2 * i + 2 # right = 2*i + 2
    # See if left child of root exists and is > root
    if l < n and a_list[i] < a_list[l]:
        largest = l
    # See if right child of root exists and is > root
    if r < n and a_list[largest] < a_list[r]:
        largest = r
    # Change root, if needed
    if largest != i:
        a_list[i],a_list[largest] = a_list[largest],a_list[i] # swap
    # Heapify the root.
        heapify(a_list, n, largest)

def heap_sort(a_list):
    n = len(a_list)
    # Build a maxheap. Since last parent will be
    # at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(a_list, n, i)
    # One by one extract elements
    for i in range(n-1, 0, -1):
        a_list[i], a_list[0] = a_list[0], a_list[i] # swap
        heapify(a_list, i, 0)


a_list = [54, 26, 93, 17, 77]
heap_sort(a_list)
print(a_list)