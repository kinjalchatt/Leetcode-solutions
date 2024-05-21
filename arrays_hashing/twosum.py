#efficient solution:

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_map = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in my_map:
                return [my_map[diff], i]
            my_map[j] = i

'''
learnings:
lookup in hashmap takes O(1) time complexity. (if diff in my_map) 
enumerate() returns (index,num) in python 

efficient approach: use hash map to instantly check for difference value, 
map will add index of last occurrence of a num, 
dont use same element twice; start with empty map and add the array nums to the map 1 by 1 by index.

brute force approach: iterate through the array twice and find the index of both numbers that add up to target 
brute force solution:
def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
'''