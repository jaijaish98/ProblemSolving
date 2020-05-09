"""

Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.val = 0
        self.kthValue = -1

    def inorder(self, root, k):
        if root == None:
            return

        self.inorder(root.left, k)

        self.val = self.val + 1
        if self.val == k:
            self.kthValue = root.val

        self.inorder(root.right, k)

    def kthSmallest(self, root, k):
        self.inorder(root, k)
        return self.kthValue


if __name__ == "__main__":
    tree = TreeNode(5,None,None)
    tree.right = TreeNode(6,None,None)
    tree.left = TreeNode(3,None,None)
    tree.left.right = TreeNode(4, None, None)
    tree.left.left = TreeNode(2, None, None)
    tree.left.left.left = TreeNode(1, None, None)
    kthSmall = Solution()
    k = 2
    print(kthSmall.kthSmallest(tree, 3))