"""
Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.res = True
        self.node = head

        def helper(root):
            if not root: return
            helper(root.next)
            if root.val != self.node.val:
                self.res = False
            self.node = self.node.next

        helper(head)
        return self.res


if __name__ == "__main__":
    Node = ListNode(1)
    Node.next = ListNode(2)
    Node.next.next = ListNode(2)
    Node.next.next.next = ListNode(1)
    palindrome = Solution()
    print(palindrome.isPalindrome(Node))
