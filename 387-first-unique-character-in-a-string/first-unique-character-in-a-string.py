from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr=Counter(s)
        for ch in s:
            if arr[ch]==1:
                return s.index(ch)
        return -1

        