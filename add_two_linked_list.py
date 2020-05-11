
"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return None
        carry = 0
        temp_head = ListNode(0)
        curr_node = temp_head
        while l1 is not None or l2 is not None:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            sum_val = (carry + v1 + v2) % 10
            carry = (carry + v1 + v2) // 10
            curr_node.next = ListNode(sum_val)
            curr_node = curr_node.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            curr_node.next = ListNode(carry)
        return temp_head.next

    def print_linked_list(self,head):
        if head is None:
            return None
        while head is not None:
            print(head.val)
            head = head.next


if __name__ == "__main__":
    l1_head = ListNode(2)
    l1 = l1_head
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2_head = ListNode(5)
    l2 = l2_head
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    ll_sum = Solution()
    sum_list = ll_sum.add_two_numbers(l1_head, l2_head)
    ll_sum.print_linked_list(sum_list)
