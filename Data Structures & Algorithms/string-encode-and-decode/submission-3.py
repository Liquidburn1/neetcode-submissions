class Solution:

    def encode(self, strs: List[str]) -> str:
        resstr=""
        for i in strs:
            resstr=resstr+str(len(i))+"#"+i
        print(resstr)
        return resstr

    def decode(self, s: str) -> List[str]:
        resarr=[]
        i=0
        while i<len(s):
            j=i
            num=""
            while s[j]!='#':
                num+=s[j]
                j+=1

            if num!="":
                j=j+1
                print("jello",num)
                resarr.append(s[j:j+int(num)])
                i=int(num)+j
        return resarr
            



            

        
