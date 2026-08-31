class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevlist={}
        for i in range(len(nums)):
            check = prevlist.get(target-nums[i],None)
            if check!= None:
                return [check,i]
            else:
                prevlist[nums[i]]=i 

        return []


            
            
            
           