# code
test_cases = int(input())
while test_cases != 0:
    arr = list(input().split('.'))
    test_cases -= 1
    l = len(arr)
    output = arr[l-1]
    for x in range(1,l):
        output = output + '.' + arr[l-1-x]
    print(output)
