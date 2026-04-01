from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op=defaultdict(list)
        op_list=[]
        for s in strs:
            sorted_s=tuple(sorted(s))
            op[sorted_s].append(s)
        for vals in op.values():
            op_list.append(vals)
        return op_list
        