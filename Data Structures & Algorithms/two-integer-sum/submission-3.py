class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        premap={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if premap.get(diff,None)!= None:
                return [premap[diff],i]
            else:
                premap[nums[i]]=i
        return []
            
           