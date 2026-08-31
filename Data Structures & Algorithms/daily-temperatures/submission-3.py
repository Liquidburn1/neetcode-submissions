class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret=[0]*len(temperatures)
        stack=[]
        
        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][0]:
                    rem=stack.pop()
                    ret[rem[1]]=(i-rem[1])
                    if len(stack)==0:
                        break
                
            stack.append((temperatures[i],i))
            
        return ret

        #stack=[(30,0),]





        
            
                


        
            
            

        
            



            
            


            
        