class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        checker={')':'(','}':'{',']':'['}
        for i in s:
            if i in checker and len(stack) !=0:
                if stack.pop() != checker[i]:
                    return False
            else:
                stack.append(i)
        if len(stack):
            return False

        return True


        