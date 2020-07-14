"""
Problem
Bangles is preparing to go on a tour of her local museum. The museum is made up of N rooms in a row,
numbered from 1 to N from left to right. The rooms are connected by N-1 locked doors,
each connecting a pair of adjacent rooms.
Each door has a difficulty level indicating how difficult it is for Bangles to open the door.
No two doors will have the same difficulty level.
The door between the i-th room and (i+1)-th room has difficulty level Di.

Bangles will pick one of the rooms to start in, and visit each of the rooms in the museum one at a time,
taking pictures as she goes. She takes a picture in her starting room,
then she repeats the following procedure until she has taken a picture in all the rooms:
Of the two locked doors available to her,
she will open the door with the lower difficulty level and take a picture in the newly unlocked room.
If there is only one locked door available to her, then she will unlock that door.
 Once a door is unlocked, it remains unlocked.

Bangles is not yet sure which room she would like to start in,
so she needs you to answer Q queries. For the i-th query,
she would like to know: What is the Ki-th room that she will take a picture in if she starts in the Si-th room?

Input
The first line of the input gives the number of test cases, T. T test cases follow.
The first line of each test case contains the two integers N and Q. The second line contains N-1 integers,
describing the locked doors. The i-th integer (starting from 1) is Di. Then, Q lines follow, describing the queries.
The i-th of these lines contains the two integers Si and Ki.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1)
and y is a list of the answers for the Q queries in order, separated by spaces.

Limits
Time limit: 40 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ Di ≤ 105, for all i.
All Di are distinct.
1 ≤ Si ≤ N, for all i.
1 ≤ Ki ≤ N, for all i.

Test set 1
2 ≤ N ≤ 1000.
1 ≤ Q ≤ 1000.

Test set 2
2 ≤ N ≤ 105 and 1 ≤ Q ≤ 105 for at most 20 test cases.
For the remaining cases, 2 ≤ N ≤ 1000 and 1 ≤ Q ≤ 1000.

Sample

Input

Output

2
5 4
90 30 40 60
3 4
3 1
1 5
4 3
10 2
6 2 4 5 9 30 7 1 8
6 8
6 8


Case #1: 5 3 5 2
Case #2: 8 8


In sample case #1, there are four queries:
In the first query, Bangle takes pictures in the rooms in the order 3, 2, 4, 5 and 1, so the answer is 5.
In the second query, Bangle takes pictures in the rooms in the order 3, 2, 4, 5 and 1, so the answer is 3.
In the third query, Bangle takes pictures in the rooms in the order 1, 2, 3, 4 and 5, so the answer is 5.
In the fourth query, Bangle takes pictures in the rooms in the order 4, 3, 2, 5, and 1, so the answer is 2.

In sample case #2, there are two queries:
In the first query, Bangle takes pictures in the rooms in the order 6, 5, 4, 3, 2, 1, 7, 8, 9 and 10, so the answer is 8.
The second query is the same as the first, so the answer is also 8.
"""

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
    head = Node(1, lval=float("inf"), rval=doors[0])
    prev = head
    dObj.store_node(1, head)
    for j in range(2, n + 1):
        curr = Node(val=j, left=prev, right=None, lval=prev.rval)
        dObj.store_node(j, curr)
        if j == n:
            curr.rval = float("inf")
        else:
            curr.rval = doors[j - 1]
        prev.right = curr
        prev = curr

    for j in range(q):
        result = []
        s, k = map(int, input().split())
        currN = dObj.get_node(s)
        curr = copy.deepcopy(currN)
        while curr is not None:
            result.append(curr.val)
            if (curr.lval == float("inf") and curr.rval == float("inf")) or (curr.left is None and curr.right is None):
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
        res.append(result[k - 1])
    print("Case #{}:".format(i + 1), *res, sep=' ')
