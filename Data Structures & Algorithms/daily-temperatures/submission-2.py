class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret=[]
        for i in range(len(temperatures)):
            found=False
            j=i+1
            while found!=True and j!=len(temperatures):
                if temperatures[j]>temperatures[i]:
                    ret.append(j-i)
                    found=True
                j+=1

            if found==False:
                    ret.append(0)
        print(temperatures)
        return ret
            
                


        
            
            

        
            



            
            


            
        