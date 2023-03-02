"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


def search_insert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low
