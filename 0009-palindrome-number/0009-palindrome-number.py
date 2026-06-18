class Solution:
    def isPalindrome(self, x: int) -> bool:
        # rev = 0
        # num = x

        # if x < 0:
        #     return False

        # while num != 0:
        #     rev = rev * 10 + num % 10
        #     rev = num // 10

        # return rev==num

        if x < 0:
            return False
        
        return str(x) == str(x)[::-1]

        
        