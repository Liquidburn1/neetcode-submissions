class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        i=0
        scount={}#{c:2,a:2,r:2,e:1}
        tcount={}#{c:2,a:2,r:2,e:1}
        while i<len(s):
            scount[s[i]]=scount.get(s[i],0)+1
            tcount[t[i]]=tcount.get(t[i],0)+1
            i+=1
        return scount==tcount
    

        