class Solution:
    def isValid(self, s: str) -> bool:

        options={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i in options:
                if not stack:
                    return False
                if stack.pop()!=options[i]:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True


        