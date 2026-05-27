from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        for i in nums:
            if hashmap[i] >= len(nums)/2:
                return i
        return
        