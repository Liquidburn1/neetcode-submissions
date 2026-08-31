class Solution:
    def isValid(self, s: str) -> bool:
        check={"}":"{","]":"[",")":"("}
        stack=[]
        for i in s:
            if i not in check:
                stack.append(i)
            else:
                if stack and stack.pop()==check[i]:
                    continue
                else:
                    return False



        if stack:
            return False
        return True