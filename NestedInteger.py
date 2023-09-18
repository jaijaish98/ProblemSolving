import collections


class NestedIterator:
    def __init__(self, nestedList):
        # Initialize a deque to store the flattened integers
        self.q = collections.deque()
        # Call the addInteger function to add integers to the deque
        self.addInteger(nestedList)

    def next(self) -> int:
        # Remove and return the leftmost element from the deque
        return self.q.popleft()

    def hasNext(self) -> bool:
        # Return True if the deque is not empty, False otherwise
        return bool(self.q)

    def addInteger(self, nestedList):
        # Iterate over the elements in the nestedList
        for ni in nestedList:
            # If the element is an integer, add it to the deque
            if ni.isInteger():
                self.q.append(ni.getInteger())
            # If the element is a list, recursively call the addInteger function to add integers to the deque
            else:
                self.addInteger(ni.getList())
