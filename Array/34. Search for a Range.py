#Author:Sun Jian

'''
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''
'''
题目要求：重复的有序数列找目标数的范围 [5, 7, 7, 8, 8, 10] 时间复杂度O(logn)
要点：二分法的衍生，取左边界：中间点小于目标数则左端+1， 大于等于目标数则右端-1，
    两端会重合在 目标数范围最左端 A或者 A左邻点B 、 重合于A时：中间点大于等于目标数 则右端-1 返回左边界A
    重合于B：中间点小于目标数  则左端+1 返回左边界A
    取右边界同理相反
    再考虑不存在的情况 会得到此时左边界大于右边界 

'''

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search_left(target,nums):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>=target:right=right-1
                else:left=left+1
            return left
        def binary_search_right(target,nums):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>target:right=right-1
                else:left=left+1
            return right
        left, right = binary_search_left(target,nums), binary_search_right(target,nums)
        return (left, right) if left <= right else [-1, -1]





