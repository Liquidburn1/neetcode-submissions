class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        valid_c={']':'[','}':'{',')':'('}
        stack=[]
        for i in s:
            if i in valid_c:
                if len(stack)==0:
                    return False
                elif stack.pop()!=valid_c[i]:
                    return False
            else:
                stack.append(i)
            print(stack)

        if len(stack)>0:
            return False
        return True


                


        

       

       







            





