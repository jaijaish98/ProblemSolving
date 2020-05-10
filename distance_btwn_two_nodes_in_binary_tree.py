"""
Find distance between two nodes in a binary tree

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.distance = 0

    def calculate_distance_of_two_nodes(self, source, dest, k=0):
        if source == None:
            return
        if source.val == dest.val:
            self.distance = k
            return
        self.calculate_distance_of_two_nodes(source.left, dest, k+1)
        self.calculate_distance_of_two_nodes(source.right, dest, k+1)
        return


    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left is not None:
            return left
        else:
            return right


if __name__ == "__main__":
    tree = TreeNode(3,None,None)
    tree.right = TreeNode(1,None,None)
    tree.left = TreeNode(4,None,None)
    tree.right.left = TreeNode(0, None, None)
    tree.right.right = TreeNode(8, None, None)
    p = tree.right
    q = tree.left
    LCA = Solution()
    LCANode = LCA.lowestCommonAncestor(tree, p, q)
    print("Ancestor of {} and {} is {}".format(p.val,q.val,LCANode.val))
    pObj = Solution()
    qObj = Solution()
    pObj.calculate_distance_of_two_nodes(LCANode, p)
    pDist =  pObj.distance
    qObj.calculate_distance_of_two_nodes(LCANode,q)
    qDist = qObj.distance
    print("Distance between {} and {} is {}".format(p.val, q.val, pDist+qDist))