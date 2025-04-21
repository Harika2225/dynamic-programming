class Solution:    
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        ans = 1.0
        N = abs(n)
        for _ in range(N):
            ans *= x
        return ans if n > 0 else 1 / ans