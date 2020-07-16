"""
Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new arr

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) space

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5,
with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference,
which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""


class Array:
    @staticmethod
    def remove_duplicates(nums):
        """
        method to remove duplicates in a given sorted array
        :param nums:
        :return array without duplicates:
        """
        if nums is None or len(nums) == 0:
            return -1
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
        return nums[:index]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9, 9]
    print(Array().remove_duplicates(arr))
