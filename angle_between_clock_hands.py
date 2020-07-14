"""
Angle Between Hands of a Clock

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

Input: hour = 12, minutes = 30
Output: 165

Input: hour = 3, minutes = 30
Output: 75

Input: hour = 4, minutes = 50
Output: 155

Input: hour = 3, minutes = 15
Output: 7.5

Input: hour = 12, minutes = 0
Output: 0
"""


class Solution:
    @staticmethod
    def angleClock(hour: int, minutes: int) -> float:
        return min(abs(30*hour-5.5*minutes),360-abs(30*hour-5.5*minutes))


if __name__ == "__main__":
    angle = Solution.angleClock(12, 30)
    print(angle)