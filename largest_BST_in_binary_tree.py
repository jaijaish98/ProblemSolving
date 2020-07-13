"""
Find largest BST in given binary tree

Given a Binary Tree, write a function that returns the size of the largest subtree which is also a Binary Search Tree.
 If the complete Binary Tree is BST, then return the size of whole tree.

 Examples:

Input:
      5
    /  \
   2    4
 /  \
1    3

Output: 3
The following subtree is the maximum size BST subtree
   2
 /  \
1    3


Input:
       50
     /    \
  30       60
 /  \     /  \
5   20   45    70
              /  \
            65    80
Output: 5
The following subtree is the maximum size BST subtree
      60
     /  \
   45    70
        /  \
      65    80
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    @staticmethod
    def find_largest_bst_in_binary_tree(head):
        if head is None:
            return 0
        ldict = {"isBST":False, "min":float("inf"), "max":float("-inf"), "size":0}
        rdict = {"isBST":False, "min":float("inf"), "max":float("-inf"), "size":0}

        def bst_util(head):
            if head is None:
                res = {"isBST":True, "min":float("inf"), "max":float("-inf"), "size":0}
                return res
            lres = bst_util(head.left)
            rres = bst_util(head.right)
            isBST = lres["isBST"] and rres["isBST"] and lres["max"] <= head.val < rres["min"]
            if isBST:
                size = lres["size"] + rres["size"] + 1
            else:
                size = max(lres["size"], rres["size"])
            minV = min(lres["min"], head.val)
            maxV = max(rres["max"], head.val)
            result = {"isBST":isBST, "min":minV, "max":maxV, "size":size}
            return result
        result = bst_util(head)
        return result["size"]


if __name__ == "__main__":
    root = TreeNode(25)
    root.left = TreeNode(18)
    root.right = TreeNode(50)
    root.left.left = TreeNode(19)
    root.left.right = TreeNode(20)
    root.left.left.right = TreeNode(15)
    root.right.left = TreeNode(35)
    root.right.left.left = TreeNode(20)
    root.right.left.left.right = TreeNode(25)
    root.right.left.right = TreeNode(40)
    root.right.right = TreeNode(60)
    root.right.right.left = TreeNode(55)
    root.right.right.right = TreeNode(70)
    bst = BST()
    size = bst.find_largest_bst_in_binary_tree(root)
    print("Largest BST size in the given binary tree is:",size)

"""
       25
     /     \
  18        50
 /  \     /    \
19   20  35     60
 \      /  \   /  \
  15   20   40 55   70
        \
         25
"""