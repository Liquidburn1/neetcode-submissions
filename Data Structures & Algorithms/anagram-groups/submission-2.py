class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret={}

        
        #convert into letters
        for i,s in enumerate(strs):
            let=[0]*26
            for c in s:
                let[ord(c)-ord('a')]+=1
            let=tuple(let)
            if let in ret:
                ret[let].append(s)
            else:
                ret[let]=[s]

        print(list(ret.values()))

        

        return list(ret.values())
                

        