"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

The main idea of solution is to use as much multiplications as possible, for example how can we evaluate x^20?
 We can just multiply x in loop 20 times, but we also can evaluate x^10 and multiply it by itself! Similarly,
 x^10 = x^5 * x^5. Now we have odd power, but it is not a problem, we evaluate x^5 = x^2 * x^2 * x.
"""


class Pow:
    def find_power(self, x, n):
        """
        Method to implement pow() method in O(log n) time
        :param x:
        :param n:
        :return: x^n
        """
        if n == 0:
            return 1
        if n < 0:
            return self.find_power(1/x, -n)
        lower = self.find_power(x, n//2)
        return lower * lower if n % 2 == 0 else lower * lower * x


if __name__ == "__main__":
    x = 2
    n = 10
    powVal = Pow().find_power(x, n)
    print(powVal)
