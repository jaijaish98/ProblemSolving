"""
 Search in Rotated Sorted Array

 Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""


class Solution:
    def search(self, nums, target):
        if len(nums) == 0 or target is None:
            return -1

        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target >= nums[start] and target < nums[mid] and nums[start] < nums[mid]:
                end = mid-1
            elif target > nums[mid] and target <= nums[end] and nums[mid] < nums[end]:
                start = mid+1
            elif (target <= nums[start] and target < nums[mid] and nums[start] <= nums[mid]) or (target > nums[mid] and target >= nums[end] and nums[mid] > nums[end]):
                start = mid+1
            else:
                end = mid-1
        return -1


if __name__ == "__main__":
    rotatedArray = Solution()
    array = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 8
    index = rotatedArray.search(array, target)
    print(index)
