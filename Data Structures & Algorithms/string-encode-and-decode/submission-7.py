class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result+=str(len(i))+"#"+i

        print(result)
        return result


    def decode(self, s: str) -> List[str]:
        i=0
        listresult=[]
        while i < len(s):
            strsize=""
            while s[i]!="#":
                strsize=strsize+s[i]
                i+=1
            size=int(strsize) #0
            i+=1
            listresult.append(s[i:(size+i)])
            i=i+size
        return listresult

            

        
