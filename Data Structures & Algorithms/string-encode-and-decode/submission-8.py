class Solution:

    def encode(self, strs: List[str]) -> str:
        ret=""
        for i in strs:
            ret+=str(len(i))+"#"+i
        return ret

    def decode(self, s: str) -> List[str]:
        i=0
        ret=[]
        while i<len(s):
            num=""
            while s[i]!="#":
                num+=s[i]
                i+=1
            i+=1
            ret.append(s[i:i+int(num)])
            i=i+int(num)
        print(ret)
        return ret
            

