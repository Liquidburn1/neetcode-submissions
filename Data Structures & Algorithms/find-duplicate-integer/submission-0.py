class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=sorted(nums)
        for i in range(len(x)):
            if i!=len(x)-1:
                if x[i]==x[i+1]:
                    return x[i]
            

        

        