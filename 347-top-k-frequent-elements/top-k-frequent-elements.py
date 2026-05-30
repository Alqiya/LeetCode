from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset=Counter(nums)
        op=[]
        i=0
        while i<k:
            max_val = max(hashset, key=hashset.get)
            op.append(max_val)
            del hashset[max_val]
            i+=1
        return op