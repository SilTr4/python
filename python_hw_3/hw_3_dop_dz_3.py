# 7 Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: int) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False
