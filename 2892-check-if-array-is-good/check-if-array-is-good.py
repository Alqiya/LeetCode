class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=max(nums)
        j=0
        for i in nums:
            if i==n:
                j+=1
        if n==1:
            if j==2:
                return True
        if j==2 and (n-1 in nums) and len(nums)==n+1:
            return True
        
        return False
        