class Solution:
    def calc(self,num2:int,num1:int,op:str) -> int:
        if op=="+":
            return num1+num2
        elif op=="-":
            return num1-num2
        elif op=="*":
            return num1*num2
        elif op=="/":
            return int(num1/num2)






    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        checker=["+","-","*","/"]
        
        for i in tokens:
            if i not in checker:
                stack.append(int(i))
            else:
                stack.append(self.calc(stack.pop(),stack.pop(),i))
        return stack[0]



        