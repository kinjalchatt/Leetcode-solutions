"""
Leetcode 217. Contains Duplicate 
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for n in nums:
            if n in my_set:
                return True
            my_set.add(n)
        return False

# Learnings:
# - Hashmap contains key-value pairs while hashset contains just a set of values.
# - Hashset only loads unique values in the set.

# Efficient approach: O(n) time complexity
# Create a hashset and iterate through the array, adding checks if any num exists in the hashset.

# Brute force approach1: O(n^2) time complexity
# Iterate through the array twice and check if nums[i] == nums[j].

# Sorting approach: O(nlogn) time complexity
# First, sort the array (nums.sort) and then iterate through the array and
# check if nums[i] == nums[i-1].
