"""
Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left is not None:
            return left
        else:
            return right


if __name__ == "__main__":
    tree = TreeNode(3,None,None)
    tree.right = TreeNode(1,None,None)
    tree.left = TreeNode(4,None,None)
    tree.right.left = TreeNode(0, None, None)
    tree.right.right = TreeNode(8, None, None)
    p = tree.right.right
    q = tree.right
    LCA = Solution()
    LCANode = LCA.lowestCommonAncestor(tree, p, q)
    print(LCANode.val)
