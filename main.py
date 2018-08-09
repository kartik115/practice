from arrays.merge_sort import merge_sort


def hasArrayTwoCandidates(A, size, sum):
    merge_sort(A, 0, size-1)
    l = 0
    r = size - 1
    while l < r:
        if A[l] + A[r] == sum:
            print(A[l], A[r])
            l = l+1
            r = r-1
        elif A[l] + A[r] < sum:
            l = l + 1
        else:
            r = r - 1


# Driver program to test the functions
A = [1, 4, 45, 6, 10, -8]
sum = 16
n = len(A)
if hasArrayTwoCandidates(A, n, sum):
    print("Array has two elements with the given sum")
else:
    print("Array doesn't have two elements with the given sum")
print(A)
