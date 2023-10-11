class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to map open to close parentheses
        parentheses_map = {
            "{": "}", 
            "(": ")", 
            "[": "]"
        }

        # Stack to help with the validation
        stack = []

        # Iterate through each character in the string
        for char in s:
            # If the character is an opening parenthesis
            if char in parentheses_map:
                stack.append(char)
            # If stack isn't empty and the character matches the closing parenthesis for the last opening one in the stack
            elif stack and char == parentheses_map[stack[-1]]:
                stack.pop()
            # If the current character doesn't match the top of the stack or the stack is empty
            else:
                return False

        # If the stack is empty, then all the parentheses were matched
        return not stack
