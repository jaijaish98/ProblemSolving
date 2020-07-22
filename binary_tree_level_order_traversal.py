"""
Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def level_order_traversal(root):
        if not root:
            return

        q = collections.deque([root, None])  # here, None will let you know the level
        tmp = []
        res = []
        while q:
            node = q.popleft()
            if node is None:
                res.append(tmp)
                tmp = []
                if q:
                    q.append(None)

            else:
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

    @staticmethod
    def create_tree():
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        return root


if __name__ == "__main__":
    print(Solution().level_order_traversal(Solution().create_tree()))
