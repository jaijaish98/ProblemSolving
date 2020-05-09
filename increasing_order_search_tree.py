"""

Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the
tree, and every node has no left child and only 1 right child.


Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.inorderArr = []

    def findInOrder(self, root):
        if root == None:
            return None
        self.findInOrder(root.left)
        self.inorderArr.append(root.val)
        self.findInOrder(root.right)

    def constructTree(self, arr):
        if len(arr) == 0:
            return
        root = TreeNode(arr[0], None, None)
        root.right = self.constructTree(arr[1:])
        return root

    def increasingBST(self, root):
        self.findInOrder(root)
        root = self.constructTree(self.inorderArr)
        return root
if __name__ == "__main__":
    tree = TreeNode(5,None,None)
    tree.right = TreeNode(6,None,None)
    tree.left = TreeNode(3,None,None)
    tree.left.left = TreeNode(2, None, None)
    tree.left.right = TreeNode(4, None, None)
    tree.right.right = TreeNode(8, None, None)
    tree.right.right.right = TreeNode(9, None, None)
    tree.right.right.left = TreeNode(7, None, None)

    increasingBST = Solution()
    root = increasingBST.increasingBST(tree)


