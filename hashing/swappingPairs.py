# Given two arrays of integers, write a program to check if a pair of values 
# (one value from each array) exists such that swapping the elements of the pair 
# will make the sum of two arrays equal.



def is_pair_exist(A, n, B, m):
	s1 = sum(A)
	s2 = sum(B)
	if (s1-s2) % 2 != 0:
		return False
	if s1 < s2:
		small = A
		large = B
		diff = (s2 - s1) // 2
	else:
		small = B
		large = A
		diff = (s1 - s2) // 2
	hash_map = dict()
	for x in range(len(small)):
		hash_map[x] = 0
	for x in range(len(large)):
		key = large[x] - diff
		if key in hash_map:
			return True
		else:
			pass
	return False


def main():
	T = int(input())
	while (T>0):
		T = T - 1
		length = list(map(int, input().split()))
		N = length[0]
		M = length[1]
		arr_1 = list(map(int, input().split()))
		arr_2 = list(map(int, input().split()))
		if is_pair_exist(arr_1, N, arr_2, M):
			print(1)
		else:
			print(-1)


if __name__ == "__main__":
	main()