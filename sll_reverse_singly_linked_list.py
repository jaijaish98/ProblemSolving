"""
Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def print_linked_list(self, head):
        result_list = []
        while head:
            result_list.append(head.val)
            head = head.next
        return  result_list


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    ll = Solution()
    print("Before reversing : {}".format(ll.print_linked_list(node)))
    rev_ll = ll.reverseList(node)
    print("After reversing : {}".format(ll.print_linked_list(rev_ll)))
