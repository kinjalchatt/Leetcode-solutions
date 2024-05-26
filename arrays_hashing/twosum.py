"""
Leetcode 1. Two Sum problem solution 
"""
#efficient solution:
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in my_map:
                return [my_map[diff], i]
            my_map[j] = i
        return []

# Efficient approach: use hash map to instantly check for difference value. O(n) time complexity
# Map will add index of last occurrence of a num, don't use same element twice.
# Start with empty map and add the array nums to the map one by one by index.

# Brute force approach: iterate through the array twice and find the index of both numbers
# that add upto target O(n^2) time complexity
