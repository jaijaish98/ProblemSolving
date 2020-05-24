"""
100 people standing in a circle in an order 1 to 100. No. 1 has a sword. He kills the next person (i.e. No. 2) and gives
the sword to the next (i.e. No. 3). All people do the same until only 1 survives. Which number survives at the last?
There are 100 people starting from 1 to 100. (N value may change)
"""


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class CLL:
    def create_cll(self, N):
        head = None
        curr = None
        for i in range(1, N+1):
            node = Node(i)
            if head is None and curr is None:
                head = node
                curr = head
                curr.next = head
            else:
                curr.next = node
                node.next = head
                curr = node
        return head

    def last_alive(self, head):
        if head is None:
            return None
        while head.next is not head:
            head.next = head.next.next
            head = head.next
        return head


if __name__ == "__main__":
    N = 100
    cll_obj = CLL()
    head = cll_obj.create_cll(N)
    last_node = cll_obj.last_alive(head)
    print(last_node.val)
