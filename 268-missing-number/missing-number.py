import numpy as np
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        arr=[]
        i,j=0,0
        for n in range(0,len(nums)+1):
            arr.append(n)
        while i<len(nums) and j<len(arr):
            if nums[i]!=arr[j]:
                return arr[j]
            i+=1
            j+=1
        if j<len(arr):
            return arr[j]