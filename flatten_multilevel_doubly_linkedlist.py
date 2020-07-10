"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL

Example 3:

Input: head = []
Output: []


How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

"""


# Definition for a Node.


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:

    def flatten_util(self, node):
        if node.child is not None:
            next_node = node.next
            node.next = node.child
            node.next.prev = node
            node.child = None
            node = self.flatten_util(node.next)
            node.next = next_node
            if next_node is not None:
                next_node.prev = node
        if node.next is None:
            return node
        else:
            node = self.flatten_util(node.next)
            return node

    def flatten(self, head):
        if head is None:
            return None
        self.flatten_util(head)
        return head

    def remove_trailing_null(self, arr):
        while len(arr)>0:
            if arr[-1] is None:
                arr.pop()
            else:
                return arr
        return arr

    def print_multilevel_doubly_linked_list(self, head):
        queue = []
        result = []

        def fill_queue(head, queue):
            while head is not None:
                queue.append(head.child)
                result.append(head.val)
                head = head.next
            result.append(None)
            queue = self.remove_trailing_null(queue)
            return queue

        queue = fill_queue(head, queue)
        while len(queue) > 0:
            node = queue.pop(0)
            if node is not None:
                queue = fill_queue(node, queue)
            else:
                result.append(None)
        result = self.remove_trailing_null(result)
        return result


    @staticmethod
    def print_doubly_linked_list(head):
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        return result


if __name__ == "__main__":
    one = head = Node(val=1)
    two = one.next = Node(val=2)
    three = two.next = Node(val=3)
    four = three.next = Node(val=4)
    five = four.next = Node(val=5)
    six = five.next = Node(val=6)
    seven = three.child = Node(val=7)
    eight = seven.next = Node(val=8)
    nine = eight.next = Node(val=9)
    ten = nine.next = Node(val=10)
    eleven = eight.child = Node(val=11)
    twelve = eleven.next = Node(val=12)
    obj = Solution()
    print(obj.print_multilevel_doubly_linked_list(head))
    obj.flatten(head)
    print(obj.print_doubly_linked_list(head))
