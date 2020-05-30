"""
Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
Example 1:

         3
       /  \
      1    4
    /    /  \
   3    1    5

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

         3
       /
     3
   /   \
 4      2

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:

    def __init__(self):
        self.count = 0

    @staticmethod
    def is_good_node(nodes):
        if len(nodes) == 0 or nodes is None:
            return False
        return True if max(nodes) == nodes[-1] else False

    def good_nodes(self, root):
        def count_good_nodes(root, nodes):
            if root is None:
                return
            nodes.append(root.val)
            self.count += self.is_good_node(nodes)
            if root.left is not None:
                count_good_nodes(root.left, nodes)
            if root.right is not None:
                count_good_nodes(root.right, nodes)
            nodes.pop()
            return

        nodes = []
        count_good_nodes(root, nodes)
        return self.count


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    obj = Solution()
    print(obj.good_nodes(root))
