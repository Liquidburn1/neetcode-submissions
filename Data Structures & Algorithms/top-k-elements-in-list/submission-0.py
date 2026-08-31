class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt={}
        for i in nums:
            dictt[i]=dictt.get(i,0)+1
        
        arr = []
        for num, cnt in dictt.items():
            arr.append((cnt, num))
        arr.sort()
        count=len(arr)-k
        
        result=[]
        while len(result) < k:
            result.append(arr.pop()[1])
        return result
        
        
        