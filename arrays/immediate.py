# code
def immediate_small_element(arr, n):
    s = None
    for i in range(n):
        if i==n-1 or arr[i] <= arr[i+1]:
            temp = str(-1) + " " 
        else:
            temp =str(arr[i+1]) + " "
        if s is None:
            s = temp
        else:
            s = s + temp
    print(s)
        

test_cases = int(input())
while test_cases != 0:
    n = int(input())
    arr = list(map(int, input().split()))
    immediate_small_element(arr, n)
    test_cases -= 1
