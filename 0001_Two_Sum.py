"""
Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Result: https://leetcode.com/submissions/detail/226689385/
"""
from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums)):
            for ptr in range(idx+1, len(nums)):
                if nums[ptr] == target - nums[idx]:
                    return idx, ptr


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))
