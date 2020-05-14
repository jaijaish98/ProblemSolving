"""
Given an array A of n elements. Find three indices i,j & k such that A[i] ^2 + A[j]^2 = A[k]^2?

"""


class Solution:
    def find_triplet_square_sum(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums = sorted(nums)
        n = len(nums)
        for i in range(n-1, 0, -1):
            my_dict = {}
            for j in range(i):
                if (nums[i] - nums[j]) in my_dict:
                    print(nums[i], nums[j], nums[i]-nums[j])
                else:
                    my_dict[nums[j]] = True


if __name__ == "__main__":
    triplet = Solution()
    nums = [1, 2, 3, 4, 5, -1, -2]
    triplet.find_triplet_square_sum(nums)
