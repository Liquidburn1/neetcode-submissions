class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret=defaultdict(list)
        for i  in strs:
            count=[0]*26
            for c in i:
                count[ord('a')-ord(c)]+=1
            ret[tuple(count)].append(i)
        
        return list(ret.values())
        


        