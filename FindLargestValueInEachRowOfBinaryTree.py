"""
Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLargestValues(self, root):
        if root == None:
            return

        largeValues = []
        stack = []

        stack.append(root)
        stack.append('X')
        maxVal = float("-inf")
        while (len(stack) >= 1):
            x = stack.pop(0)
            if x == 'X':
                largeValues.append(maxVal)
                stack.append('X')
                maxVal = float("-inf")
                if (len(stack) == 1):
                    return largeValues
            else:
                if x.val > maxVal:
                    maxVal = x.val
                if x.left != None:
                    stack.append(x.left)
                if x.right != None:
                    stack.append(x.right)
        return largeValues


if __name__ == "__main__":
    tree = TreeNode(1,None,None)
    tree.right = TreeNode(2,None,None)
    tree.left = TreeNode(3,None,None)
    tree.right.right = TreeNode(9, None, None)
    tree.left.left = TreeNode(5, None, None)
    tree.left.right = TreeNode(3, None, None)
    largeValues = Solution()
    largeValuesArr = largeValues.findLargestValues(tree)
    print(largeValuesArr)

