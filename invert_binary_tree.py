"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

#Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_binary_tree(self, root):
        if root==None:
            return
        root.left, root.right = self.invert_binary_tree(root.right), self.invert_binary_tree(root.left)
        return root

    def inorder_traversal(self, root):
        if root==None:
            return
        self.inorder_traversal(root.left)
        print(root.val)
        self.inorder_traversal(root.right)


if __name__ == "__main__":
    tree = TreeNode(4,None,None)
    tree.right = TreeNode(7,None,None)
    tree.left = TreeNode(2,None,None)
    tree.right.right = TreeNode(9, None, None)
    tree.right.left = TreeNode(6, None, None)
    tree.left.right = TreeNode(3, None, None)
    tree.left.left = TreeNode(1, None, None)
    invert = Solution()
    invert.invert_binary_tree(tree)
    invert.inorder_traversal(tree)
