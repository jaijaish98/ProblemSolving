"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

Convert Sorted Array to Binary Search Tree

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return
        if len(nums)==1:
            root = TreeNode(nums[0],None,None)
        mid = len(nums)//2
        root = TreeNode(nums[mid],None,None)
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


if __name__ == "__main__":
    minimalTree = Solution()
    arr = [-10,-3,0,5,9]
    root = minimalTree.sortedArrayToBST(arr)
