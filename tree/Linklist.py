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

    # Given a singly linked list, find middle of the linked list
    # If there are even nodes, then there would be two middle nodes, we need to print second middle element.
    def findMid(self):
        head = self.head
        # Code here
        if head is None:
            return -1
        curr = head
        mid = None
        count = 0
        while curr is not None:
            count += 1
            if count % 2 == 0:
                # mid element change only if count is even
                if count == 2:
                    mid = curr
                else:
                    mid = mid.next
            else:
                # mid element remain same
                if count == 1:
                    mid = curr
                else:
                    pass
            curr = curr.next
        return mid


l = LinkList()
l.head = Node(10)
l.head.next = Node(29)
l.head.next.next = Node(40)
l.head.next.next.next = Node(8)
print("print list")
l.print_list()
print("print reverse list")
l.reverse()
l.print_list()
print("get middle node")
print(l.findMid().value)
