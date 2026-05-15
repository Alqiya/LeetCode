class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        carry=0
        for p in range(len(nums)-1,-1,-1):
            if nums[p]==9:
                nums[p]=0
                carry=1
            else:
                nums[p]+=1
                return nums
        if carry==1:
            nums.insert(0,1)
        return nums
        