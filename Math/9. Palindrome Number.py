#Author:Sun Jian

'''
Determine whether an integer is a palindrome. Do this without extra space.

'''


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10 ==0 and x!=0 ):
            return False

        else:
            s=0
            p=x
            while p>0:
                s=s*10+p%10
                p//=10
            return s==x

