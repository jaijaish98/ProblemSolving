"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

"""


class Solution:
    def largestRectangleArea(self, histograms):
        stack = []
        max_area = 0
        index = 0
        while index < len(histograms):
            if (not stack) or (histograms[stack[-1]] <= histograms[index]):
                stack.append(index)
                index += 1
            else:
                top = stack.pop()
                area = (histograms[top] * ((index - stack[-1] - 1) if stack else index))
                max_area = max(area, max_area)
        while stack:
            top = stack.pop()
            area = (histograms[top] * ((index - stack[-1] - 1) if stack else index))
            max_area = max(area, max_area)
        return max_area

    def maximalRectangle(self, matrix):
        max_area = 0
        if len(matrix) < 1:
            return 0
        row = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if int(matrix[i][j]) == 1:
                    row[j] = row[j] + int(matrix[i][j])
                else:
                    row[j] = 0
            max_area = max(max_area, self.largestRectangleArea(row))
        return max_area


if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    rec_matrix = Solution()
    max_area = rec_matrix.maximalRectangle(matrix)
    print(max_area)

