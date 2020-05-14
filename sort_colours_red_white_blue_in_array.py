"""
Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

"""


class Solution:
    def sort_colors(self, nums):
        start = 0
        end = len(nums) - 1
        red = start - 1
        blue = end + 1
        while start <= end:
            if nums[start] == 0:
                nums[red + 1], nums[start] = nums[start], nums[red + 1]
                red = red + 1
                start = start + 1
            elif nums[start] == 2:
                nums[start], nums[blue - 1] = nums[blue - 1], nums[start]
                end = end - 1
                blue = blue - 1
            else:
                start = start + 1
        return nums


if __name__ == "__main__":
    colours = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    nums = colours.sort_colors(nums)
    print(nums)
