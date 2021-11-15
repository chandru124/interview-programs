class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        
        match = { '{' : '}', '[' : ']', '(': ')'}
        stack = []
        for c in s:
            if c in match:
                stack.append(c)
            else:
                if len(stack) <= 0 or match[stack.pop()] != c:
                    return False
            
        if len(stack) == 0:
            return True
        return False
