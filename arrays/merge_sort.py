def merge_sort(A, l, r):
    if l < r:
        m = int((l + r) / 2)
        merge_sort(A, l, m)
        merge_sort(A, m+1, r)
        merge(A, l, m, r)


def merge(A, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = A[left + i]
    for j in range(0, n2):
        R[j] = A[mid + 1 + j]
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        k += 1
        j += 1
    while i < n1:
        A[k] = L[i]
        k += 1
        i += 1


# Driver program to test the functions
# A = [1, 4, 45, 6, 10, -8]
# n = len(A)
# merge_sort(A, 0, n-1)
# print(A)
