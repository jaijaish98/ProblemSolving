"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16


"""


class Solution:
    def islandPerimeter(self, grid):
        row = len(grid)
        col = len(grid[0])
        p = 0
        for i in range(row):
            for j in range(col):
                up, down, right, left = 0, 0, 0, 0
                if grid[i][j] == 1:
                    if i == 0:
                        up = 1
                    if i == row - 1:
                        down = 1
                    if i > 0 and grid[i - 1][j] == 0:
                        up = 1
                    if i < row - 1 and grid[i + 1][j] == 0:
                        down = 1
                    if j == 0:
                        left = 1
                    if j == col - 1:
                        right = 1
                    if j > 0 and grid[i][j - 1] == 0:
                        left = 1
                    if j < col - 1 and grid[i][j + 1] == 0:
                        right = 1
                p += up + down + left + right
        return p


if __name__ == "__main__":
    island = Solution()
    arr = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(island.islandPerimeter(arr))