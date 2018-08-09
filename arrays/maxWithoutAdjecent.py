# Given an array of positive numbers, find the maximum sum of a subsequence
# with the constraint that no 2 numbers in the sequence should be adjacent in the array.


def max_stolen_value_from_house(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i-2]+arr[i], dp[i-1])

    return dp[-1]


test_cases = int(input())
while test_cases != 0:
    arr = list(map(int, input().split()))
    print(max_stolen_value_from_house(arr, len(arr)))
    test_cases -= 1
