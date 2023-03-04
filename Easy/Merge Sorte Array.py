"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
 representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
 To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
 and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
from typing import List


# Do not return anything, modify nums1 in-place instead.

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i in range(n):
        nums1[m + i] = nums2[i]
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]  # Marcin Curia's gap sequence
    for gap in gaps:
        for i in range(gap, len(nums1)):
            j = i
            while j >= gap and nums1[j] < nums1[j - gap]:
                nums1[j], nums1[j - gap] = nums1[j - gap], nums1[j]
                j -= gap
    return


# the solution on leetcode.com :-
# https://leetcode.com/problems/merge-sorted-array/solutions/3255616/python3-shell-sort-algorithm-33ms/?orderBy=most_votes
