import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        word = re.sub(r'[^0-9a-zA-Z]+', '', s).lower()
        print(word)
        return word == word[::-1]

        
        