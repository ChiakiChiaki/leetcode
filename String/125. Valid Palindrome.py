#Author:Sun Jian
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.


'''

'''
题目要求：判断字符串是否回文 只考虑文字数字 不考虑其他字符
要点： 过滤出文字数字 用str.isalnum()判断 
       可以循环遍历过滤  
       也可以用filter ，filter() 函数用于过滤序列 语法filter(function, iterable)
       py3中filter返回filter类 可以看成是一个迭代器
       

'''


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = filter(str.isalnum, s.lower())
        s = [c for c in s]
        return s == s[::-1]



# class Solution:
#     def isPalindrome(self, s):
#         s=[c.lower() for c in s if c.isalnum()]
#         return s==s[::-1]









