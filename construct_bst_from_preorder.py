"""
Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sliceLeftNodes(self, arr, rootVal):
        start, end = 0, 0
        if len(arr) == 0:
            return [None]
        for i in range(len(arr)):
            if arr[i] < rootVal:
                end = i+1

        return arr[start:end]

    def sliceRightNodes(self, arr, rootVal):
        start, end = len(arr), len(arr)
        if len(arr) == 0:
            return [None]
        for i in range(len(arr)):
            if arr[i] >= rootVal:
                start = i
                break
        return arr[start:end]

    def bstFromPreorder(self, preorder):
        if len(preorder) == 0:
            return None
        if len(preorder)==1:
            root = TreeNode(preorder[0], None, None)
            return root
        root = TreeNode(preorder[0], None, None)
        lArr = self.sliceLeftNodes(preorder[1:], root.val)
        rArr = self.sliceRightNodes(preorder[1:], root.val)
        root.left = self.bstFromPreorder(lArr)
        root.right = self.bstFromPreorder(rArr)
        return root

    def inorderTraversal(self, root):
        if root == None:
            return
        self.inorderTraversal(root.left)
        print(root.val)
        self.inorderTraversal(root.right)

if __name__ == "__main__":
    preOrder = Solution()
    arr = [8,5,1,7,10,12]
    root = preOrder.bstFromPreorder(arr)
    preOrder.inorderTraversal(root)