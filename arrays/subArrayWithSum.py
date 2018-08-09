# Given an unsorted array of non-negative integers, 
# find a continuous sub-array which adds to a given number.

# Input:
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10

# Output:
# 2 4
# 1 5

def find_subarray_index(array, total, size):
	first = 0
	last = 0
	current_sum = array[0]
	for x in range(1, size):
	    #print(current_sum, first, last)
	    if current_sum < total:
	    	current_sum += array[x]
	    	last += 1
	    while current_sum > total:
	        current_sum -= array[first]
	        first += 1
	    if current_sum == total:
	       return first, last
	return -1, -1


test_cases = int(input())
for x in range(test_cases):
	ip = list(map(int, input().split()))
	n = ip[0]
	total = ip[1]
	array = list(map(int, input().split()))
	f,l = find_subarray_index(array, total, n)
	if f == l == -1:
		print(-1)
	else:
		print(f+1, l+1)