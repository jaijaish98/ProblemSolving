"""
Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s) or len(s) == 0 or len(p) == 0:
            return None
        s_dic = {}
        p_dic = {}
        result = []
        for i in range(97, 123):
            s_dic[chr(i)] = 0
            p_dic[chr(i)] = 0
        for i in p:
            p_dic[i] += 1
        for i in range(len(p)):
            s_dic[s[i]] += 1
        if s_dic == p_dic:
            result.append(0)
        for i in range(len(p), len(s)):
            s_dic[s[i - len(p)]] -= 1
            s_dic[s[i]] += 1
            if p_dic == s_dic:
                result.append(i - len(p) + 1)
        return result

    def print_anagrams(self, s, indices, l):
        result = []
        for i in indices:
            result.append(s[i:i+l])
        return result


if __name__ == "__main__":
    anagrams = Solution()
    s = "cbaebabacd"
    p = "abc"
    anagram_index_arr = anagrams.findAnagrams(s, p)
    result = anagrams.print_anagrams(s, anagram_index_arr, len(p))
    print(result)

