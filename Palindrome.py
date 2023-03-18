class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversedNum = 0
        Num=x
        while x > 0:
            reversedNum = reversedNum * 10 + x % 10
            x = x // 10

        return True if (Num == reversedNum) else False