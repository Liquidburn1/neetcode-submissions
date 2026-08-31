class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        checker={'}':'{',']':'[',')':'('}
        for i in s:
            if i in checker:
                if stack:
                    if checker[i]!=stack.pop():
                        return False
                else:
                    return False
            else:
                stack.append(i)
        if len(stack)!=0:
            return False
        
        return True

        
        