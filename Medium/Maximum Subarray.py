"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""
from typing import List


def max_subarray(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)
