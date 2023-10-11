class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pare = {
                "{":"}", 
                "(":")", 
                "[":"]",
                }
        
        stack = []

        # lifo

        for i in s:

            if stack and stack[-1] in ["}","]",")"]: 
                return False
            elif stack and pare[stack[-1]] == i:
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0
        
        