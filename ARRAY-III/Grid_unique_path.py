class Solution(object):
    def uniquePaths(self, m, n):
        N = n + m - 2     # Total steps
        r = m - 1         # Number of down moves
        res = 1
        for i in range(1, r + 1):
            res = res * (N - r + i) / i
        return int(res)