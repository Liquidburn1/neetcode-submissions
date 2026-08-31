class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1

        res=[]
        for i in count.items():
            res.append((i[1],i[0]))
        res.sort()
        print(res)
        result=[]
        i=0
        j=len(res)-1
        while i < k:
            result.append(res[j][1])
            i+=1
            j-=1
            
        return result

        

        
        

            


    


        