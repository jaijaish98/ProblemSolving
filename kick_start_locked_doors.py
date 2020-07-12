import copy


class Node:
    ddd = {}
    def __init__(self, val, left=None, right=None, lval=0, rval=0):
        self.val = val
        self.left = left
        self.right = right
        self.lval = lval
        self.rval = rval


class DDD:
    def __init__(self):
        self.ddd = {}

    def store_node(self, val, node):
        self.ddd[val] = node

    def get_node(self, val):
        return self.ddd[val]


tc = int(input())
for i in range(tc):
    n, q = map(int, input().split())
    doors = list(map(int, input().split()))
    res = []
    dObj = DDD()
    head = Node(1,lval=float("inf"), rval=doors[0])
    prev = head
    dObj.store_node(1, head)
    for j in range(2,n+1):
        curr = Node(val=j, left=prev, right=None, lval=prev.rval)
        dObj.store_node(j,curr)
        if j==n:
            curr.rval = float("inf")
        else:
            curr.rval = doors[j-1]
        prev.right = curr
        prev = curr

    for j in range(q):
        result = []
        s, k = map(int, input().split())
        currN = dObj.get_node(s)
        curr = copy.deepcopy(currN)
        while curr is not None:
            result.append(curr.val)
            if (curr.lval==float("inf") and curr.rval==float("inf")) or (curr.left is None and curr.right is None):
                curr = None
            elif curr.lval < curr.rval:
                temp = curr
                curr = curr.left
                curr.right = temp.right
                curr.rval = temp.rval
                if curr.right is not None:
                    curr.right.left = temp.left
            else:
                temp = curr
                curr = curr.right
                curr.left = temp.left
                curr.lval = temp.lval
                if curr.left is not None:
                    curr.left.right = temp.right
        res.append(result[k-1])
    print("Case #{}:".format(i + 1),*res, sep=' ')