class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={} # mapping charCount to list of Anagrams

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c) - ord("a")]+=1
            tup=tuple(count)
            if result.get(tup,None) != None:
                result[tup].append(s)
            else:
                result[tup]=[s]
        return list(result.values())
        

            
            
            
        