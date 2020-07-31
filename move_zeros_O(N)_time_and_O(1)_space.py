"""
Move Zeroes
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the
relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""


class Array:
    @staticmethod
    def move_zeroes(nums):
        def find_zero_index(array, prev, last):
            for itr in range(prev, last):
                if array[itr] == 0:
                    return itr
            return last

        if nums is None or len(nums) == 0:
            return None
        zeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                zeroIndex = find_zero_index(nums, zeroIndex, i)
                if zeroIndex < i:
                    nums[zeroIndex], nums[i] = nums[i], nums[zeroIndex]
                    zeroIndex += 1
        return nums


if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    print(Array().move_zeroes(arr))
