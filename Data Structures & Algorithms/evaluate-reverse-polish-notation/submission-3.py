class Solution:

    def calc(self,num1:int,num2:int,operator:str):
        if operator=="+":
            return num1+num2
        elif operator=="-":
            return num1-num2
        elif operator=="*":
            return num1*num2
        else:
            return int(num1/num2)

    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=["+","-","*","/"]
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                a=stack.pop()
                b=stack.pop()
                stack.append(self.calc(b,a,i))
        print(stack)
        return stack.pop()
                




        
        