'''

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).



'''
'''
3Sum Closest 题目要求：数字列表取3个数 相加之和距离目标数最接近(假设就一个结果) 返回3个数的和
要点：  取前三个数的和作为初始数   类似3Sum 遍历求和与初始数比较 更

'''


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        length=len(nums)

        if length < 3:
            return None
        temp=nums[0]+nums[1]+nums[2]

        for i,v in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if i>length-3:
                break
            l=i+1
            r=length-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum==target:
                    return sum
                elif abs(sum-target)<abs(temp-target):
                    temp=sum
                if sum<target:
                    l=l+1
                    while l < r  and nums[l] == nums[l - 1]:
                        l = l + 1
                else:
                     r=r-1
                     while l<r and nums[r] == nums[r+1]:
                         r=r-1

        return temp



