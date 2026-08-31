class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        scount={}
        tcount={}
        i=0
        j=0
        while i < len(s):
            scount[s[i]]=scount.get(s[i],0)+1
            tcount[t[j]]=tcount.get(t[i],0)+1

            i+=1
            j+=1
        if scount==tcount:
            return True
        else:
            return False



        