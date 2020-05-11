"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    @staticmethod
    def two_sum(nums, target):
        if len(nums) < 1:
            return None
        result_arr = []
        my_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in my_dict:
                result_arr.append(i)
                result_arr.append(nums.index(target - nums[i]))
                break
            else:
                my_dict[nums[i]] = i
        result_arr = sorted(result_arr)
        return result_arr


if __name__ == "__main__":
    two_sum = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result_index = two_sum.two_sum(nums, target)
    print(result_index)
