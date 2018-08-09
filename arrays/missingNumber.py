# Given an array of size n-1 and given that there are numbers from 1 to n with one missing, 
# the missing number is to be found.


def find_missing_number(arr, n):
	total = sum(arr)
	desired_value = n * (n+1) /2 
	return desired_value - total

test_cases = int(input())
for x in range(test_cases):
	n = int(input())
	array = list(map(int, input().split()))
	print(find_missing_number(array, n))
