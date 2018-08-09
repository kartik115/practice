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

    def reverse(self):
        curr = self.head
        prev = None
        new = None
        while curr is not None:
            new = curr.next
            curr.next = prev
            prev = curr
            curr = new
        self.head = prev


l = LinkList()
l.head = Node(10)
l.head.next = Node(29)
l.head.next.next = Node(40)
l.head.next.next.next = Node(8)
l.print_list()
l.reverse()
l.print_list()