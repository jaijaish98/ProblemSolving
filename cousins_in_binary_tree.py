"""
Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Input: root = [1,2,3,4], x = 4, y = 3
    1
   / \
  2   3
 /
4
Output: false

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4

          1
        /  \
       2    3
       \     \
        4     5
Output: true
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.arr = [False, 0, -1]

    def findElement(self, root, ele, k=0, parent=-1):
        if root == None:
            self.arr = [False, -1, -1]
            return self.arr
        elif root.val == ele:
            self.arr = [True, k, parent]
            return self.arr
        self.arr = self.findElement(root.left, ele, k + 1, root.val)
        if self.arr[0] != False:
            return self.arr
        return self.findElement(root.right, ele, k + 1, root.val)

    def isCousins(self, root: TreeNode, x, y) :
        xArr = self.findElement(root, x, 0, -1)
        yArr = self.findElement(root, y, 0, -1)
        # print(xArr,yArr)
        if (xArr[0] == yArr[0] == True) and (xArr[1] == yArr[1]) and (xArr[2] != yArr[2]):
            return True
        return False

if __name__ == "__main__":
    tree = TreeNode(1,None,None)
    tree.right = TreeNode(3,None,None)
    tree.left = TreeNode(2,None,None)
    tree.left.right = TreeNode(4, None, None)
    tree.right.right = TreeNode(5, None, None)
    x, y = 4, 5
    cousins = Solution()
    isCousins = cousins.isCousins(tree, x, y)
    print(isCousins)
