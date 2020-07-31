"""
Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

"""


class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)

    def intersect(self, nums1, nums2):

        def find_intersect(nums1, nums2):

            result = []
            hashMap = {}

            for i in range(len(nums1)):
                if hashMap.get(nums1[i]):
                    hashMap[nums1[i]] += 1
                else:
                    hashMap[nums1[i]] = 1

            for i in range(len(nums2)):
                if hashMap.get(nums2[i]):
                    if hashMap[nums2[i]] > 0:
                        hashMap[nums2[i]] -= 1
                        result.append(nums2[i])

            return result

        if len(nums1) > len(nums2):
            return find_intersect(nums2, nums1)
        else:
            return find_intersect(nums1, nums2)


if __name__ == "__main__":
    inter = Solution()
    nums1 = [4, 9, 5, 9]
    nums2 = [9, 4, 9, 8, 4]
    result_arr = inter.intersection(nums1, nums2)
    print(result_arr)
    print(inter.intersect(nums1, nums2))
