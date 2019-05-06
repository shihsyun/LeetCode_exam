"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

Result: https://leetcode.com/submissions/detail/227121683/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        z = x
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x = int(x/10)
        return z == y


x = 121
solution = Solution()
print(solution.isPalindrome(x))

x = -121
solution = Solution()
print(solution.isPalindrome(x))

x = 10
solution = Solution()
print(solution.isPalindrome(x))

x = 11
solution = Solution()
print(solution.isPalindrome(x))
