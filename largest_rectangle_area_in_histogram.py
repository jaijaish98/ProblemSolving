"""
Largest Rectangle in Histogram

                   6
             5   ______
           ______|     |
           |     |     |        3
  2        |     |     |  2  ______
_____   1  |     |     |_____|     |
|    |_____|     |     |     |     |
|    |     |     |     |     |     |
|----|-----|-----|-----|-----|-----|-----
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

                   6
             5   ______
           ______|_____|
           |/ / /|/ / /|        3
  2        |/ / /|/ / /|  2  ______
_____   1  |/ / /|/ / /|_____|     |
|    |_____|/ / /|/ / /|     |     |
|    |     |/ / /|/ / /|     |     |
|----|-----|-----|-----|-----|-----|-----
"""


class Solution:
    def largestRectangleArea(self, histograms):
        stack = []
        max_area = 0
        index =0
        while index < len(histograms):
            if (not stack) or (histograms[stack[-1]] <= histograms[index]):
                stack.append(index)
                index += 1
            else:
                top = stack.pop()
                area = (histograms[top] *((index- stack[-1] - 1) if stack else index))
                max_area = max(area, max_area)
        while stack:
            top = stack.pop()
            area = (histograms[top] *((index- stack[-1] - 1) if stack else index))
            max_area = max(area, max_area)
        return max_area


if __name__ == "__main__":
    histogram = Solution()
    print(histogram.largestRectangleArea([2, 1, 5, 6, 2, 3]))

