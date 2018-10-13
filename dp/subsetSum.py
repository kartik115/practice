def is_subset(arr, n):
    total = 0
    for x in range(n):
        total += arr[x]
    if total % 2 != 0:
        return False
    total = int(total / 2)
    sum_arr = [[False for x in range(n + 1)] for y in range(total + 1)]
    for row in range(n + 1):
        sum_arr[row][0] = True
    for col in range(1, total + 1):
        sum_arr[0][col] = False

    for x in range(1, n + 1):
        for y in range(1, total + 1):
            if y < arr[x - 1]:
                sum_arr[x][y] = sum_arr[x - 1][y]
            else:
                sum_arr[x][y] = sum_arr[x - 1][y - arr[x - 1]] or sum_arr[x - 1][y]
    return sum_arr[n][total]


def main():
    T = int(input())
    while (T > 0):
        T = T - 1
        N = int(input())
        arr = list(map(int, input().split()))
        if is_subset(arr, N):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
