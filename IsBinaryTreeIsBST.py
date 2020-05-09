"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

    2
   / \
  1   3

Input: [2,1,3]
Output: true

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        return self.bst_helper(root, float("-inf"), float("inf"))

    def bst_helper(self, node, mini, maxi):

        if node is None:
            return True

        if node.val < mini or node.val > maxi:
            return False

        return (self.bst_helper(node.left, mini, node.val - 1) and
                self.bst_helper(node.right, node.val + 1, maxi))


if __name__ == "__main__":
    tree = TreeNode(1,None,None)
    tree.right = TreeNode(4,None,None)
    tree.left = TreeNode(1,None,None)
    tree.right.left = TreeNode(3, None, None)
    tree.right.right = TreeNode(6, None, None)
    BST = Solution()
    isBST = BST.isValidBST(tree)
    print(isBST)
