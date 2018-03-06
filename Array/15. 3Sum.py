#Author:Sun Jian

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

'''
题目要求:数字列表取3个数 和等于0，所有不重复组合
要点: sort排序容易去重, 循环遍历数组，固定遍历点A，B=A+1 C=len(list)-1 再让BC往中间靠，ABC都要注意去重，遇到重复的跳过


'''


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        """
        length=len(nums)
        result=[]
        if length<3:
            return result
        nums.sort()
        for i,v in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if i>=length-2:
                break
            l=i+1
            r=length-1
            while l<r:
                s=v + nums[l] + nums[r]
                if s == 0:
                    result.append([v,nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l=l+1
                    while l<r and nums[r]==nums[r-1]:
                        r=r-1
                    l = l + 1
                    r = r - 1

                elif s < 0:
                    l=l+1
                    while l<r and nums[l]==nums[l-1]:
                        l=l+1

                else:
                    r=r-1
                    while l<r and nums[r]==nums[r+1]:
                        r=r-1

        return  result



