"""
Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Result: https://leetcode.com/submissions/detail/226930069/
"""
from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashtable = dict()
        for idx, value in enumerate(nums):
            subvalue = target - value
            if subvalue in hashtable:
                return idx, hashtable[subvalue]
            else:
                hashtable[value] = idx


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))

nums = [3, 2, 4]
target = 6
solution = Solution()
print(solution.twoSum(nums, target))

nums = [-10, -1, -18, -19]
target = -19
solution = Solution()
print(solution.twoSum(nums, target))
