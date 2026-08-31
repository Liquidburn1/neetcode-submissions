class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        scount={}
        tcount={}
        for i in range(0,len(s)):
            
            scount[s[i]]=scount.get(s[i],0)+1
            tcount[t[i]]=tcount.get(t[i],0)+1
        if scount!=tcount:
            return False
        return True
        