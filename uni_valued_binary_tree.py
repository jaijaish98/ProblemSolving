"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    unique = -1
    isUniValue = True

    def assignUnique(self, val):
        self.unique = val

    def checkIsUnivalTree(self, root):
        if root == None:
            return
        self.checkIsUnivalTree(root.left)
        if root.val != self.unique:
            self.isUniValue = False
            return
        self.checkIsUnivalTree(root.right)

    def isUnivalTree(self, root):
        self.assignUnique(root.val)
        self.checkIsUnivalTree(root)
        return self.isUniValue

if __name__ == "__main__":
    tree = TreeNode(0,None,None)
    tree.right = TreeNode(0,None,None)
    tree.left = TreeNode(0,None,None)
    tree.left.left = TreeNode(0, None, None)
    tree.left.right = TreeNode(0, None, None)
    tree.right.left = TreeNode(1, None, None)
    tree.right.right = TreeNode(0, None, None)
    uniValueTree = Solution()
    print(uniValueTree.isUnivalTree(tree))
