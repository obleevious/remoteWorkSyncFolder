#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
#
# algorithms
# Easy (40.19%)
# Total Accepted:    42.1K
# Total Submissions: 104.8K
# Testcase Example:  '[0,0,0,1]'
#
# In a given integer array nums, there is always exactly one largest element.
# 
# Find whether the largest element in the array is at least twice as much as
# every other number in the array.
# 
# If it is, return the index of the largest element, otherwise return -1.
# 
# Example 1:
# 
# 
# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the
# array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return
# 1.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return
# -1.
# 
# 
# 
# 
# Note:
# 
# 
# nums will have a length in the range [1, 50].
# Every nums[i] will be an integer in the range [0, 99].
# 
# 
# 
# 
#
class Solution:
    def dominantIndex(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2:
            return 0
        lgst, sgst = max(nums[0], nums[1]), min(nums[0], nums[1])
        if nums[0] > nums[1]:
            li, si = 0, 1
        else:
            li, si = 1, 0
        for i in range(2, len(nums)):
            num = nums[i]
            if num > lgst:
                sgst, lgst = lgst, num
                si, li = li, i
            elif num > sgst:
                sgst = num
                si = i
        
        return li if lgst >= sgst * 2 else -1