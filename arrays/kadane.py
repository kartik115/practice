# Write an efficient program to find the sum of contiguous subarray
# within a one-dimensional array of numbers
# which has the largest sum.


def max_subarray_sum(arr, n):
    max_so_far = None
    max_ending_here = 0
    for i in range(n):
        max_ending_here = max_ending_here + arr[i]
        if max_so_far is None or max_ending_here > max_so_far:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

test_cases = int(input())
while test_cases != 0:
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_subarray_sum(arr, n))
    test_cases -= 1



