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


def merge_sort(List):
    mid = int(len(List) / 2)
    if len(List) <= 1: return List
    return merge(merge_sort(List[:mid]), merge_sort(List[mid:]))

def merge(l1, l2):
    final = []
    l1 = sorted(l1)
    l2 = sorted(l2)
    while l1 and l2:
        if l1[0] <= l2[0]:
            final.append(l1.pop(0))
        else:
            final.append(l2.pop(0))
    return final + l1 + l2

def main():
    L = [22, 11, 44,55, 33, 66, 100, 200]
    print(merge_sort(L))


if __name__ == "__main__":
    main()