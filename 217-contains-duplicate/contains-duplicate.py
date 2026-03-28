class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        op={}
        for n in nums:
            op[n]=op.get(n,0)+1
            if op[n]==2:
                return True
                break
        return False
        