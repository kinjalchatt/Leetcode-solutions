"""
Leetcode 242. Valid Anagram Problem Solution 
"""

# Efficient solution:


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if strings have different length they cannot be anagrams
        if len(s) != len(t):
            return False
        countS, countT = {}, {}  # created two hashmaps for counting chars from s and t
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  # filling the hashmaps
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for (
            c
        ) in (
            countS
        ):  # checking every character in the hashmap countS if it equals characters from countT hashmap or not
            if countS[c] != countT.get(c, 0):
                return False
        return True


# Sorting solution:
# return  sorted(s) == sorted(t)
# - might be asked to write your own sorting algorithm

# Learnings:
# - get() returns the value of specified key from hashmap.
# - using get() you can pass a default value of 0 to handle keyerror.

# Efficient approach: O(n) time complexity
# - In this problem, brute force and efficient have its pros and cons and both are mentioned below.
# - We can make O(1) space complexity by using sorting but that is gonna increase time to O(nlogn) time complexity.
# - Use a hashmap and count the characters in both s and t and store them in the hashmap and just check for equality.
# - However, this takes O(s+t) space complexity as we are creating two hashmaps but gives us the better O(n) time complexity.
