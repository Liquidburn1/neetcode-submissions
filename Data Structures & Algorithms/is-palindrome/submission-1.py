class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=""
        for c in s:
            if c.isalnum():
                newstr+=c.lower()
        
        i=0

        j=len(newstr)-1
        while i < len(newstr):
            if newstr[i]==newstr[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        


        

        