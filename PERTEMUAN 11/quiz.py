# merge sort

def mergeSort(A):
    print("Membelah ", A)
    n = len(A)
    if (n < 2):
        return
    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]
    mergeSort(left)
    mergeSort(right)
    i = 0
    j = 0
    k = 0
    while (i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            A[k] = left[i]
            i = i+1
        else:
            A[k] = right[j]
            j = j+1
        k = k+1
    while (i < len(left)):
        A[k] = left[i]
        i = i+1
        k = k+1
    while (j < len(right)):
        A[k] = right[j]
        j = j+1
        k = k+1
    print("Menggabungkan ", A)

A = [3, 5, 2, 5, 7, 8, 1, 0, 4, 14, 3, 5, 12, 5, 9, 8, 11, 10, 5, 1,
13, 1, 8, 5, 7, 2, 1, 0, 0, 41]


mergeSort(A)
print(A)

# binary search

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1

x = 13

result = binarySearch(A, 0, len(A)-1, x)


if result != -1:
    print("Element is present at index", str(result))

