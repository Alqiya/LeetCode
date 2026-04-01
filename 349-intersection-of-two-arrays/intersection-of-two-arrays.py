class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # op={}
        # op_list=[]
        # for n in nums1:
        #     op[n]=1
        # for n in nums2:
        #     if n in op and n not in op_list:
        #         op_list.append(n)
        # return op_list

        s1=set(nums1)
        s2=set(nums2)
        return list(s1&s2)

