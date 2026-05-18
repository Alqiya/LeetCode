class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        for p in range(len(s)-1,-1,-1):
            if s[p]==" ":
                if length==0:
                    continue
                else:
                    return length
            else:
                length+=1
        return length
            
            

        