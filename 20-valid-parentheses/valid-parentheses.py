class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for p in s:
            if p in ("([{"):
                stack.append(p)
            else:
                if not stack:
                    return False
                popped=stack.pop()
                
                if popped=="(" and p==")":
                    continue
                elif popped=="{" and p=="}":
                    continue
                elif popped=="[" and p=="]":
                    continue
                else:
                    return False
        return len(stack) == 0
            

        