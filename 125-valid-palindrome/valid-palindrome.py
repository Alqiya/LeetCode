class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_str=s.lower()
        op=[]
        for let in my_str:
            if let.isalnum() :
                op.append(let)
                
        l,r=0,len(op)-1
        while l<r:
            if op[l]!=op[r]:
                return False
            l+=1
            r-=1
        return True
        
                