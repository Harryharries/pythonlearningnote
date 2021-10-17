#!/usr/bin/env python
# -*-encoding:utf-8-*-
# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# def merge_sort(List):
#     mid = int(len(List) / 2)
#     if len(List) <= 1: return List
#     return merge(merge_sort(List[:mid]), merge_sort(List[mid:]))

# def merge(l1, l2):
#     final = []
#     l1 = sorted(l1)
#     l2 = sorted(l2)
#     while l1 and l2:
#         if l1[0] <= l2[0]:
#             final.append(l1.pop(0))
#         else:
#             final.append(l2.pop(0))
#     return final + l1 + l2


def merge(list, l, m, r):
    # Merges two subarrays of arr[].
    # First subarray is arr[l..m]
    # Second subarray is arr[m+1..r]
    n1 = m - l + 1
    n2 = r - m

    subarray1 = [None] * n1
    subarray2 = [None] * n2

    # Copy data to temp arrays 'subarray'

    for i in range(0,n1):
        subarray1[i] = list[l+i]
    
    for j in range(0,n2):
        subarray2[j] = list[m+1+j]

        # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i<n1 and j<n2:
        if subarray1[i] <= subarray2[j]:
            list[k] = subarray1[i]
            i += 1
        else:
            list[k] = subarray2[j]
            j += 1
        k+=1

    while i < n1:
        list[k] = subarray1[i]
        i += 1
        k += 1
    while j < n2:
        list[k] = subarray2[j]
        j += 1
        k += 1


def merge_sort(list, l, r):

    if l < r:
        mid = (l+r)//2
        merge_sort(list,l,mid)
        merge_sort(list,mid+1,r)
        merge(list, l, mid, r)

def ready_merge_sort(list):
    # mid = len(list) // 2
    l = 0
    r = len(list)-1

    merge_sort(list, l, r)

def main():
    L = [0, 11, 44,55, 33, 66, 100, 200]
    ready_merge_sort(L)
    print(L)

if __name__ == "__main__":
    main()