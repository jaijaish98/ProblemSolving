"""
  Find All Duplicates in an Array
  Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class Solution:
    @staticmethod
    def find_duplicates(nums):
        i = 0
        while i<len(nums):
            if i==nums[i]-1 or nums[i]==nums[nums[i]-1]:
                i+=1
            else:
                temp = nums[i]-1
                nums[i], nums[temp] = nums[temp], nums[i]
        return [nums[it] for it in range(len(nums)) if it != nums[it] - 1]


if __name__ == "__main__":
    arr = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().find_duplicates(arr))
