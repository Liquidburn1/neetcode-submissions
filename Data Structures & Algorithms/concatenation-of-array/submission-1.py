class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length=len(nums)

        ans=[0]*2*length
        i=0
        arr=[]
        while i< length:
            ans[i]=ans[i+length]=nums[i]
            i+=1

        return ans
            


        