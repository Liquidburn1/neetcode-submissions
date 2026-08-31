class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
        #count={7:2}
        resarr=[]
        for v,c in count.items():
            resarr.append((c,v))
        resarr.sort()
        print(resarr)
        
        out=len(resarr)-1
        final=[]
        while k!=0:
            final.append(resarr[out][1])
            out-=1
            k-=1
        return final
            


        

        


        

        