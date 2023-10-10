import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        word = ''.join(char for char in s if char.isalnum()).lower()
        return word == word[::-1]

        
        