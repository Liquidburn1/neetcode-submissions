class Solution:

    def encode(self, strs: List[str]) -> str:
        ret=""
        for i in strs:
            ret=ret+str(len(i))+"#"+i

        print(ret)
        return ret

            

    def decode(self, s: str) -> List[str]:
        ret=[]
        i=0

        while i<len(s):
            count=""
            while s[i]!='#':
                count+=s[i]
                i+=1
            size=int(count)
            ret.append(s[i+1:i+1+size])
            i+=size+1
        return ret




            
