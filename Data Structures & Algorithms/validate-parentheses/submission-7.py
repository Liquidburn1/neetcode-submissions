class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        toclose={")":"(","}":"{","]":"["}
        for i in s:
            if toclose.get(i,None) == None:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False

                else:
                    if stack.pop()!= toclose[i]:
                        return False

        if len(stack)>0:
            return False
        return True

       







            





