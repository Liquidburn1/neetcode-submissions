class Solution:

    def encode(self, strs: List[str]) -> str:

        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        c=0
        while c<len(s):
            counter=""
            while s[c]!="#":
                counter+=s[c]
                c+=1
            c+=1
            #counter=5
            #c=1
            res.append(s[c:c+int(counter)])
            c=c+int(counter)

            
        return res
