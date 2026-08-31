class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt={}
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            

            key = tuple(count)
            if dictt.get(key,None) !=None:
               dictt.get(key).append(s)
            else:
                dictt[tuple(count)]=[s] 
        
        return list(dictt.values())
                

        