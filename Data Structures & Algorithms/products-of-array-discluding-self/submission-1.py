class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zcount=0
        product=1
        for i in nums:
            if i!=0:
                product*=i
            else:
                zcount+=1
            
        if (zcount>1):
            return [0]*len(nums)
        
        res=[]
        for i in range(len(nums)):
            if nums[i]==0:
                res.append(int(product))
            elif nums[i]!=0 and zcount>0:
                res.append(0)
            else:
                res.append(int(product/nums[i]))
                
        return res


        