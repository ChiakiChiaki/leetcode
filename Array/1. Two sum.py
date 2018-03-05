#Author:Sun Jian

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
'''
题目要求: 给定目标数 从数字列表中取两个数相加等于目标(假设就一个精确结果) 返回索引的形式

dict 时间复杂度O(1)
造一个对应字典 {"A数与目标数的差":"A数在列表的索引"}
遍历数组 如果B数存在于字典的键中 则表示与A相加为目标数 、则返回A、B在数组中的索引   不存在则按形式添加入字典
'''


class Solution:
    def twosum(self,nums,target):
        sum_dict={}
        for i,v in enumerate(nums):
            if v in sum_dict:
                return [sum_dict[v],i]
            else:
                sum_dict[target-v] = i

