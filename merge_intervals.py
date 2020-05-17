"""
Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""


class Solution:
    def merge(self, intervals):
        if len(intervals) == 1:
            if len(intervals[0]) == 0:
                return None
        intervals = sorted(intervals)
        index = 0
        while index < len(intervals) - 1:
            if intervals[index][0] <= intervals[index + 1][0] <= intervals[index][1]:
                intervals[index][1] = max(intervals[index + 1][1], intervals[index][1])
                intervals.pop(index + 1)
            else:
                index += 1
        return intervals


if __name__ == "__main__":
    intervals = Solution()
    _intervals = [[1, 3], [2, 6], [6, 10], [6, 18]]
    result = intervals.merge(_intervals)
    print(result)
