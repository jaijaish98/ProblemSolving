"""
 Construct Binary Tree from Inorder and Postorder Traversal
 Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""
#Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def find_index(self, val, arr):
        try:
            return arr.index(val)
        except ValueError:
            return -1

    def buildTree(self, inorder, postorder):

        if len(postorder) < 1:
            return

        rootVal = postorder.pop()
        rootIndex = self.find_index(rootVal, inorder)
        root = TreeNode(rootVal)
        root.left = self.buildTree(inorder[:rootIndex], postorder[:rootIndex])
        root.right = self.buildTree(inorder[rootIndex + 1:], postorder[rootIndex:])
        return root


if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    tree = Solution()
    root = tree.buildTree(inorder, postorder)
