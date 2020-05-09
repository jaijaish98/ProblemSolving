"""
Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def updateDiameter(self, root):
        if root == None:
            return 0

        leftH = self.updateDiameter(root.left)
        rightH = self.updateDiameter(root.right)
        if leftH + rightH > self.maxDiameter:
            self.maxDiameter = leftH + rightH

        return max(leftH, rightH) + 1

    def diameterOfBinaryTree(self, root):
        self.updateDiameter(root)
        return self.maxDiameter

if __name__ == "__main__":
    tree = TreeNode(1,None,None)
    tree.right = TreeNode(3,None,None)
    tree.left = TreeNode(2,None,None)
    tree.left.left = TreeNode(4, None, None)
    tree.left.left = TreeNode(5, None, None)
    diameter = Solution()
    maxDiameter = diameter.diameterOfBinaryTree(tree)
    print(maxDiameter)