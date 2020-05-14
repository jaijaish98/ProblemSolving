"""
Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6


Example 2:

Input: [1,2,3,4]
Output: 24
"""


class Solution:
    @staticmethod
    def maximum_product(self, nums):
        if len(nums)<3:
            return None
        nums = sorted(nums)
        p1 = nums[0]*nums[1]*nums[-1]
        p2  = nums[-3]*nums[-2]*nums[-1]
        return p1 if p1 > p2 else p2


if __name__ == "__main__":
    prod = Solution()
    nums = [1, 2, 3, 4, -5, -3]
    max_prod = prod.maximum_product(nums)
    print(max_prod)
