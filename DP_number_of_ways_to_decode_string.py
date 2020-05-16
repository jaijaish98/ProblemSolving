"""
Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""


class Solution:
    def _dp_helper(self, data, dp):
        # Base Case 1: Empty string
        if not data:
            return 1

        first_call, second_call = 0, 0

        if data in dp:
            return dp[data]

        if 1 <= int(data[:1]) <= 9:
            first_call = self._dp_helper(data[1:], dp)

        if 10 <= int(data[:2]) <= 26:
            second_call = self._dp_helper(data[2:], dp)

        dp[data] = first_call + second_call

        return dp[data]

    def numDecodings(self, s: str) -> int:
        dp = {}
        if not s:
            return 0
        return self._dp_helper(s, dp)


if __name__ == "__main__":
    decoding = Solution()
    print(decoding.numDecodings("226"))
