class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        op={}
        for n in nums:
            op[n]=op.get(n,0)+1
        for n in nums:
            if op[n]==1:
                return n
        

