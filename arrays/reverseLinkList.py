class Node:

    def __init__(self, data):
        self.value = data
        self.next = None


class LinkList:

    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next

    def add_values(self, values, length):
        curr = self.head
        for x in range(length):
            temp = Node(values[x])
            if curr is None:
                self.head = temp
                curr = self.head
            else:
                curr.next = temp
                curr = curr.next


# Given a linked list, write a function to reverse every k nodes 
# (where k is an input to the function).If a linked list is given as 
# 1->2->3->4->5->6->7->8->NULL and k = 3 then output will be 3->2->1->6->5->4->8->7->NULL.
def reverse(head, k):
	current = head
	previous = None
	upcoming = None
	first = None
	count = 0

	while current is not None and count < k:
		count += 1
		upcoming = current.next
		current.next = previous
		previous = current
		current = upcoming
	if current is not None:
		head.next = reverse(current, k)
	return previous
        

if __name__ == "__main__":
    T = int(input())
    while (T>0):
        T = T - 1
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        l = LinkList()
        l.add_values(arr, n)
        l.head = reverse(l.head, k)
        l.print_list()
