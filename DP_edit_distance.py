"""
Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution:
    @staticmethod
    def min_distance(word1, word2):

        dp = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]
        dp[0][0] = 0

        for i in range(1, len(dp)):
            dp[i][0] = i

        for j in range(1, len(dp[0])):
            dp[0][j] = j

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    pass
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[-1][-1]


if __name__ == "__main__":
    dist = Solution()
    s1 = "jaijaish98"
    s2 = "jayendran"
    print("Minimum edit required to change {} to {} is {}".format(s1, s2, dist.min_distance(s1, s2)))
