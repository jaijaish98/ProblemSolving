"""

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    range_sum = 0

    def rangeSumBST(self, root, L, R):
        if root == None:
            return
        self.rangeSumBST(root.left, L, R)
        if root.val <= R and root.val >= L:
            self.range_sum += root.val
        self.rangeSumBST(root.right, L, R)
        return self.range_sum

if __name__ == "__main__":
    tree = TreeNode(5,None,None)
    tree.right = TreeNode(10,None,None)
    tree.left = TreeNode(3,None,None)
    tree.left.left = TreeNode(1, None, None)
    tree.left.right = TreeNode(4, None, None)
    tree.right.left = TreeNode(8, None, None)
    tree.right.right = TreeNode(15, None, None)
    rangeSum = Solution()
    L , R = 10,30
    rangeSum = rangeSum.rangeSumBST(tree,L,R)
    print(rangeSum)
