"""
Pseudo-Palindromic Paths in a Binary Tree

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic
 if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:
         2
       /  \
      3    1
    /  \    \
   3    1    1
Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree.
There are three paths going from the root node to leaf nodes:
the red path [2,3,3], the green path [2,1,1], and the path [2,3,1].
Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3]
can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
              2
            /  \
          1     1
        /  \
       1    3
             \
              1
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree.
There are three paths going from the root node to leaf nodes:
the green path [2,1,1], the path [2,1,3,1], and the path [2,1].
Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:

Input: root = [9]
Output: 1
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.path_count = 0

    @staticmethod
    def can_palindromic(node_list):
        dic = {}
        odd_count = 0
        for i in range(1, 10):
            dic[i] = 0
        for i in node_list:
            dic[i] = dic[i] + 1
        for i in range(1, 10):
            if (dic[i] % 2) != 0:
                odd_count += 1
        if odd_count <= 1:
            print(node_list)
            return True
        else:
            return False

    def pseudo_palindromic_paths(self, root):
        def find_pseudo_palindromic_paths_count(root, node_list):
            if node_list is not None and len(node_list) > 0:
                if root.right is None and root.left is None:
                    self.path_count += self.can_palindromic(node_list)
                    node_list.pop()
                    return
                else:
                    if root.right is not None:
                        node_list.append(root.right.val)
                        find_pseudo_palindromic_paths_count(root.right, node_list)
                    if root.left is not None:
                        node_list.append(root.left.val)
                        find_pseudo_palindromic_paths_count(root.left, node_list)
                    if node_list is not None:
                        node_list.pop()
            return
        node_list = [root.val]
        find_pseudo_palindromic_paths_count(root, node_list)
        return self.path_count


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(1)
    obj = Solution()
    print(obj.pseudo_palindromic_paths(root))
