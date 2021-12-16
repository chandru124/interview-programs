class Solution:
    def climbStairs(self, n: int, steps = [1, 2], memo = {}) -> int:
        if n in memo: return memo[n]
        if n == 0: return 1
        if n < 0: return 0

        count = 0
        for step in steps:
            count += self.climbStairs(n - step, steps, memo)
            
        memo[n] = count

        return count
