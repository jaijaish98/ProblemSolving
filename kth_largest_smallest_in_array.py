"""
Kth Largest/Smallest Element in an Array

Find the kth largest/smallest element in an unsorted array. Note that it is the kth largest element in the sorted order,
 not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output:
    largest element =  5
    smallest element =  2
"""


class Solution:
    def find_kth_largest(self, nums, k):
        if k > len(nums):
            return None
        nums = sorted(nums)
        return nums[len(nums) - k]

    def find_kth_smallest(self, nums, k):
        if k > len(nums):
            return None
        nums = sorted(nums)
        return nums[k-1]


if __name__ == "__main__":
    obj = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k =2
    kth_large = obj.find_kth_largest(nums, k)
    kth_small = obj.find_kth_smallest(nums, k)
    print("Kth largest element is {} \nKth smallest element is {}".format(kth_large, kth_small))
