"""
Binary Tree Top View

Given a binary tree, imagine yourself standing on the top of it, return the values of the nodes
you can see ordered from right to left.

Input: [1,2,3,null,5,null,4]
Output: [2,1,3,4]
Explanation:

   1
 /   \
2     3
 \     \
  5     4
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
        self.topViewArray = []
        self.levelDict = {}

    def extract_top_node_values(self):
        od = collections.OrderedDict(sorted(self.levelDict.items()))
        for i in od:
            self.topViewArray.append(self.levelDict[i])

    def find_top_view_of_binary_tree(self, root=None, k=0):
        if root==None:
            return
        if k not in self.levelDict:
            self.levelDict[k] = root.val
        self.find_top_view_of_binary_tree(root.left, k-1)
        self.find_top_view_of_binary_tree(root.right, k+1)

    def top_side_view(self, root):
        if root==None:
            return
        self.find_top_view_of_binary_tree(root, 0)
        self.extract_top_node_values()
        return self.topViewArray



if __name__ == "__main__":
    tree = TreeNode(1,None,None)
    tree.right = TreeNode(3,None,None)
    tree.left = TreeNode(2,None,None)
    tree.right.right = TreeNode(4, None, None)
    tree.left.right = TreeNode(5, None, None)

    topView = Solution()
    topViewArray = topView.top_side_view(tree)
    print(topViewArray)
