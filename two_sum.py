"""
Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Sum:
    @staticmethod
    def two_sum(nums, target):
        hashMap = {}
        result = []
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                result.append(hashMap[target - nums[i]])
                result.append(i)
            else:
                hashMap[nums[i]] = i
        return result


if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    target = 22
    print(Sum().two_sum(arr, target))

