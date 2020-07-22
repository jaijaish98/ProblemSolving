"""
Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right,
then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


from binary_tree_level_order_traversal import *

if __name__ == "__main__":
    root = Solution().create_tree()
    result = Solution().level_order_traversal(root)
    for i in range(len(result)):
        if i % 2 != 0:
            result[i] = result[i][::-1]
    print(result)
