from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        op=Counter(nums)
        hashset=set(nums)

        for k,v in op.items():
            if v==1:
                hashset.remove(k)
        return list(hashset)

        