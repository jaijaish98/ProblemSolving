"""
Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""


class Solution:
    def frequencySort(self, s):
        if len(s) < 1:
            return ""
        dic = {}
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1
        res = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]))
        res_str = ""
        for i in range(len(res) - 1, -1, -1):
            res_str += (res[i][0] * res[i][1])
        return res_str


if __name__ == "__main__":
    sort = Solution()
    print(sort.frequencySort("aaAbbbc"))
