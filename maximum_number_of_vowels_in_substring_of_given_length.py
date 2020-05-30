"""
Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
Example 4:

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.
Example 5:

Input: s = "tryhard", k = 4
Output: 1
"""


class Solution:
    @staticmethod
    def find_vowels_count(s):
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in s:
            if i in vowels:
                count += 1
        return count

    def max_vowels(self, s, k):
        if k <= 0 or len(s) == 0 or s == "" or s is None or k > len(s):
            return 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        max_count = count = self.find_vowels_count(s[0:k])
        for i in range(k, len(s)):
            if count == k:
                return count
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            max_count = max(count, max_count)
        return max_count


if __name__ == "__main__":
    obj = Solution()
    s = 'leetcode'
    k = 3
    print(obj.max_vowels(s, k))
