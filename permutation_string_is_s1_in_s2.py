"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""


class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > 0 and len(s2) == 0:
            return False
        if len(s1) > len(s2):
            return False
        s1_dic = {}
        s2_dic = {}
        for i in range(26):
            s1_dic[chr(97 + i)] = 0
            s2_dic[chr(97 + i)] = 0
        for i in range(len(s1)):
            s1_dic[s1[i]] = s1_dic[s1[i]] + 1
        for i in range(len(s1)):
            s2_dic[s2[i]] = s2_dic[s2[i]] + 1
        for i in range(0, len(s2)):
            if s1_dic == s2_dic:
                return True
            else:
                # if i+len(s1) <= len(s2):
                s2_dic[s2[i]] = s2_dic[s2[i]] - 1
                s2_dic[s2[((i + len(s1)) % len(s2))]] = s2_dic[s2[((i + len(s1)) % len(s2))]] + 1
        return False


if __name__ == "__main__":
    permutation= Solution()
    print(permutation.checkInclusion("adc", "dcda"))
