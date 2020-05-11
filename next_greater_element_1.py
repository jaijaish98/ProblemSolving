"""
Next Greater Element I

ou are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

"""


class Solution:

    @staticmethod
    def next_greater_element(nums_1, nums_2):
        if len(nums_1) < 1 or len(nums_2) < 1:
            return None

        my_dict = {}
        stack = []
        for i in range(0, len(nums_2)):
            if len(stack) == 0:
                stack.append(nums_2[i])
            else:
                while len(stack) > 0:
                    x = stack.pop()
                    if nums_2[i] > x:
                        my_dict[x] = nums_2[i]
                    else:
                        stack.append(x)
                        break
                stack.append(nums_2[i])
        while len(stack) > 0:
            x = stack.pop()
            my_dict[x] = -1
        result_arr = []
        for i in nums_1:
            result_arr.append(my_dict[i])
        return result_arr


if __name__ == "__main__":
    nextGre = Solution()
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    resultArr = nextGre.next_greater_element(nums1, nums2)
    print(resultArr)
