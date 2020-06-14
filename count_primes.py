"""
 Count Primes
 Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""

import math


class Solution:
    def __init__(self):
        pass

    def count_primes(self, n: int) -> int:
        if n<=1:
            return 0
        prime = []
        for i in range(2,n):
            flag=0
            for val in prime:
                if val<=math.sqrt(i):
                    if i%val==0:
                        flag=1
                        break
                else:
                    break
            if flag==0:
                prime.append(i)
        return len(prime)


if __name__ == "__main__":
    prime = Solution()
    print(prime.count_primes(1000))
