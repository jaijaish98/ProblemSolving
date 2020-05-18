"""
 Intersection of Two Linked Lists

 Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

     1 -> 2-> 3->|
                 |
           1->2->4->5->6
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        l1 = 0
        l2 = 0
        t1 = headA
        t2 = headB
        while t1 is not None:
            l1 += 1
            t1 = t1.next
        while t2 is not None:
            l2 += 1
            t2 = t2.next
        if l1 >= l2:
            diff = l1 - l2
            t1 = headA
            t2 = headB
        else:
            diff = l2 - l1
            t1 = headB
            t2 = headA

        while diff > 0:
            t1 = t1.next
            diff -= 1
        while t1 is not None and t2 is not None:
            if t1 == t2:
                return t1
            t1 = t1.next
            t2 = t2.next
        return None


if __name__ == "__main__":
    L1 = ListNode(1)
    L1.next = ListNode(2)
    L1.next.next = ListNode(3)
    L1.next.next.next = ListNode(4)
    L1.next.next.next.next = ListNode(5)
    L2 = ListNode(0)
    L2.next = ListNode(1)
    L2.next.next = ListNode(2)
    L2.next.next.next = L1.next.next
    Intersection = Solution()
    node = Intersection.getIntersectionNode(L1, L2)

