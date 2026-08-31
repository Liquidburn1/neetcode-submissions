class Solution:
    def isValid(self, s: str) -> bool:
        values={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:

            if i in values:
                if len(stack) == 0 or stack.pop()!=values[i]:
                    return False
            else:
                stack.append(i)

        if len(stack)>0:
            return False
        return True
        
        