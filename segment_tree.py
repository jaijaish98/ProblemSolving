"""
------------------------------------------Contributed by Jayendran(jaijaish98)------------------------------------------
A Segment Tree is a data structure that allows answering range queries over an array effectively,
while still being flexible enough to allow modifying the array.
This includes finding the sum of consecutive array elements a[l…r],
or finding the minimum element in a such a range in O(log n) time.
Between answering such queries the Segment Tree allows modifying the array by replacing one element,
or even change the elements of a whole subsegment (e.g. assigning all elements a[l…r] to any value,
or adding a value to all element in the subsegment).

In general a Segment Tree is a very flexible data structure, and a huge number of problems can be solved with it.
Additionally it is also possible to apply more complex operations and answer more complex queries
(see Advanced versions of Segment Trees). In particular the Segment Tree can be easily generalized to larger dimensions.
For instance with a two-dimensional Segment Tree you can answer sum or minimum queries over some sub rectangle of
a given matrix. However only in O(log2n) time.

One important property of Segment Trees is, that they require only a linear amount of memory.
The standard Segment Tree requires 4n vertices for working on an array of size n.
"""


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.min = float("inf")
        self.max = float("-inf")
        self.sum = float("inf")
        self.leftEdge = None
        self.rightEdge = None


class SegmentTree:
    def __init__(self):
        """
        Initializer method to initialize the class level objects
        :rtype: object
        """
        self.partial_overlap = "Partial overlap"
        self.no_overlap = "No overlap"
        self.complete_overlap = "Complete overlap"

    def get_overlap(self, x1, y1, x2, y2):
        """
        Method to get the overlapping type for a given ranges
        X1, Y1 -> Given node's range
        X2, Y2 -> Query range
        :return: type of overlap
        """
        if (x1 == x2 and y1 == y2) or (x1 >= x2 and y1 <= y2):
            overlap = self.complete_overlap
        elif (y1 < x2) or (x1 > y2):
            overlap = self.no_overlap
        else:
            overlap = self.partial_overlap
        return overlap

    def construct_segment_tree(self, array, start, end):
        """
        Method to construct a Segment tree using a given array elements
        :param end:
        :param start:
        :param array: Array elements
        :return: Root node of a segment tree
        """
        if end - start <= 0 or len(array) == 0:
            return None
        if end - start == 1:
            node = Node()
            node.min = array[start]
            node.max = array[start]
            node.sum = array[start]
            node.leftEdge = start
            node.rightEdge = end - 1
            return node
        else:
            node = Node()
            mid = start + (end - start) // 2
            node.left = self.construct_segment_tree(array, start=start, end=mid)
            node.right = self.construct_segment_tree(array, start=mid, end=end)
            if node.left is None and node.right is None:
                node.sum = 0
                node.leftEdge = start
                node.rightEdge = start
                node.min = float("inf")
                node.max = float("-inf")
            elif node.left is None:
                node.sum = node.right.sum
                node.leftEdge = node.right.leftEdge
                node.rightEdge = node.right.rightEdge
                node.min = node.right.min
                node.max = node.right.max
            elif node.right is None:
                node.sum = node.left.sum
                node.leftEdge = node.left.leftEdge
                node.rightEdge = node.left.rightEdge
                node.min = node.left.min
                node.max = node.left.max
            else:
                node.min = min(node.left.min, node.right.min)
                node.max = max(node.left.max, node.right.max)
                node.sum = node.left.sum + node.right.sum
                node.leftEdge = node.left.leftEdge
                node.rightEdge = node.right.rightEdge
            return node

    def update_segment_tree(self, head, index, new_value, array):
        """
        Method to update the segment tree node value
        :return: Head node of a segment tree
        :rtype: object
        """
        if index == head.leftEdge == head.rightEdge:
            head.max = new_value
            head.min = new_value
            head.sum = new_value
            array[index] = new_value
            return head
        elif (head.leftEdge <= index <= head.rightEdge) and (head.rightEdge > head.leftEdge):
            left_node = self.update_segment_tree(head=head.left, index=index, new_value=new_value, array=array)
            right_node = self.update_segment_tree(head=head.right, index=index, new_value=new_value, array=array)
            head.sum = right_node.sum + left_node.sum
            head.min = min(left_node.min, right_node.min)
            head.max = max(left_node.max, right_node.max)
            return head
        else:
            return head

    def get_minimum(self, head, left, right):
        """
        Method to get the minimum in a given range query
        :return: Minimum value for a given range query
        """
        overlap = self.get_overlap(head.leftEdge, head.rightEdge, left, right)
        if overlap == self.complete_overlap:
            return head.min
        elif overlap == self.no_overlap:
            return float("inf")
        elif overlap == self.partial_overlap:
            left_min = self.get_minimum(head=head.left, left=left, right=right)
            right_min = self.get_minimum(head=head.right, left=left, right=right)
            return min(left_min, right_min)

    def get_maximum(self, head, left, right):
        """
        Method to get the maximum value for a given range query
        :return Maximum value for a given range query
        """
        overlap = self.get_overlap(head.leftEdge, head.rightEdge, left, right)
        if overlap == self.complete_overlap:
            return head.max
        elif overlap == self.no_overlap:
            return float("-inf")
        elif overlap == self.partial_overlap:
            left_max = self.get_maximum(head=head.left, left=left, right=right)
            right_max = self.get_maximum(head=head.right, left=left, right=right)
            return max(left_max, right_max)

    def get_sum(self, head, left, right):
        """
        Method to return the sum of an array elements for a given range query
        :return: Returns the sum of an array elements for a given range query
        """
        overlap = self.get_overlap(head.leftEdge, head.rightEdge, left, right)
        if overlap == self.complete_overlap:
            return head.sum
        elif overlap == self.no_overlap:
            return 0
        elif overlap == self.partial_overlap:
            left_sum = self.get_sum(head=head.left, left=left, right=right)
            right_sum = self.get_sum(head=head.right, left=left, right=right)
            return left_sum + right_sum

    def preorder_traversal(self, head, array):
        if head is None:
            return
        print("Array = {} Min = {}, Max = {}, Sum = {}".format(array[head.leftEdge:head.rightEdge + 1], head.min,
                                                               head.max, head.sum))
        self.preorder_traversal(head=head.left, array=array)
        self.preorder_traversal(head=head.right, array=array)


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70]
    st = SegmentTree()
    root = st.construct_segment_tree(array=arr, start=0, end=len(arr))
    left_index = 0
    right_index = 4
    update_index = 0
    update_value = 200
    print(st.get_sum(head=root, left=left_index, right=right_index))
    print(st.get_minimum(head=root, left=left_index, right=right_index))
    st.update_segment_tree(head=root, index=update_index, new_value=update_value, array=arr)
    print(st.get_maximum(head=root, left=left_index, right=right_index))
    st.preorder_traversal(root, arr)
