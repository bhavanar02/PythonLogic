class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        prev, curr = 1, 2
        for _ in range(n-2):
            prev, curr = curr, prev+curr
        return curr