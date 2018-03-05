#Author:Sun Jian

'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''


'''
题目要求：反转数字 过大返回0 
要点：字符串可以直接[::-1]反转 直接取绝对值反转 ；负号交给cmp处理，cmp()在3.X版本被取代，cmp(x,y) :(x>y)-(x<y)

'''

class Solution:
    def reverse(self, x):
        x=((x>0)-(x<0))*int(str(abs(x)[::-1]))
        return x if abs(x)<=2**31 else 0