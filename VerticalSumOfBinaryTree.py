"""
Find vertical sum of a binary tree
"""
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.verDict = {}
        self.verticalArray = []

    def findVerticalTraversal(self, root, k):
        if root == None:
            return
        if k not in self.verDict:
            l = []
            l.append(root.val)
            self.verDict[k] = l
        else:
            self.verDict[k].append(root.val)
        self.findVerticalTraversal(root.left, k - 1)
        self.findVerticalTraversal(root.right, k + 1)

        return

    def convertDictToList(self):
        od = collections.OrderedDict(sorted(self.verDict.items()))
        for i in od:
            self.verticalArray.append(sum(self.verDict[i]))

    def verticalTraversal(self, root):
        if root == None:
            return
        self.findVerticalTraversal(root, 0)
        self.convertDictToList()
        return self.verticalArray


if __name__ == "__main__":
    tree = TreeNode(1,None,None)
    tree.right = TreeNode(3,None,None)
    tree.left = TreeNode(2,None,None)
    tree.right.right = TreeNode(4, None, None)
    tree.left.right = TreeNode(5, None, None)

    verticalSum = Solution()
    verticalSumArr = verticalSum.verticalTraversal(tree)
    print(verticalSumArr)
