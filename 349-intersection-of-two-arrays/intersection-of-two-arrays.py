class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        op={}
        op_list=[]
        for n in nums1:
            op[n]=op.get(n,0)+1
        for n in nums2:
            if n in op_list:
                continue
            elif n not in op_list:
                if n in op.keys():
                    op_list.append(n)
            
        return op_list
