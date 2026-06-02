class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        op=''
        
        while i<len(word1) and j<len(word2):
            op+=word1[i]
            op+=word2[j]
            i+=1
            j+=1
        
        op+=word1[i:]
        op+=word2[j:]
        
        return op
        