class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x={}
        for i in range(len(nums)):
            diff=target-nums[i]
            
            if x.get(diff)!=None:
                
                return [x.get(diff),i]
            else:
                x[nums[i]]=i
        return []