"""
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min_depth = float("inf")

    def find_min_depth(self, root, k):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            if self.min_depth > k:
                self.min_depth = k
        self.find_min_depth(root.left, k + 1)
        self.find_min_depth(root.right, k + 1)
        return

    def minDepth(self, root):
        if root == None:
            return 0
        self.find_min_depth(root, 1)
        return self.min_depth


if __name__ == "__main__":
    tree = TreeNode(3,None,None)
    tree.right = TreeNode(20,None,None)
    tree.left = TreeNode(9,None,None)
    tree.right.left = TreeNode(15, None, None)
    tree.right.right = TreeNode(7, None, None)
    depth = Solution()
    minDepth = depth.minDepth(tree)
    print(minDepth)
