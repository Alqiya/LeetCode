class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=1
        while r<len(nums):
            if nums[l]==nums[r]:
                nums.pop(r)
                l=r
                r+=1
                self.removeDuplicates(nums)
            else:
                l=r
                r+=1
        return len(nums)

 
        