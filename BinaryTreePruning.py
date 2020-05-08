"""
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Solution
class Solution:
    def pruneTree(self, root):
        if root==None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left == None and root.right == None:
            return None
        return root
    def inorderTraversal(self,root):
        if root == None:
            return
        self.inorderTraversal(root.left)
        print(root.val)
        self.inorderTraversal(root.right)

if __name__ == "__main__":
    tree = TreeNode(0,None,None)
    tree.right = TreeNode(1,None,None)
    tree.left = TreeNode(1,None,None)
    tree.left.left = TreeNode(0, None, None)
    tree.left.right = TreeNode(1, None, None)
    tree.right.left = TreeNode(1, None, None)
    tree.right.right = TreeNode(0, None, None)
    pruning = Solution()
    pruning.pruneTree(tree)
    pruning.inorderTraversal(tree)