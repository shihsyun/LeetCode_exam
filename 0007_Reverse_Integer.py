"""
Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Result: https://leetcode.com/submissions/detail/227046721/
"""


class Solution:
    def reverse(self, x: int) -> int:

        X_MAX = 2**31 - 1
        X_MIN = -2**31 - 1

        if x < 0:
            x = -1*int(str(0-x)[::-1])
        else:
            x = int(str(x)[::-1])

        if x > X_MAX or x < X_MIN:
            return 0

        return x


x = 123
solution = Solution()
print(solution.reverse(x))

x = -123
solution = Solution()
print(solution.reverse(x))

x = 120
solution = Solution()
print(solution.reverse(x))
