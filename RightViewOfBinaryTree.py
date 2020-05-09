"""
Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
you can see ordered from top to bottom.

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        if root == None:
            return None
        rightView = []
        stack = []
        stack.append('X')
        stack.append(root)

        while (len(stack) > 1):
            node = stack.pop(0)
            if (node == 'X'):
                viewNode = stack.pop(0)
                rightView.append(viewNode.val)
                stack.append('X')
                if viewNode.right != None:
                    stack.append(viewNode.right)
                if viewNode.left != None:
                    stack.append(viewNode.left)
            else:
                if node.right != None:
                    stack.append(node.right)
                if node.left != None:
                    stack.append(node.left)
        return rightView


if __name__ == "__main__":
    tree = TreeNode(1,None,None)
    tree.right = TreeNode(3,None,None)
    tree.left = TreeNode(2,None,None)
    tree.right.right = TreeNode(4, None, None)
    tree.left.right = TreeNode(5, None, None)

    rightView = Solution()
    rightViewArray = rightView.rightSideView(tree)
    print(rightViewArray)
