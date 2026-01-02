n = 10000
k = 15
dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[1] = list(range(n + 1))
for i in range(2, k + 1):
    dp[i][1] = 1
    for j in range(2, n + 1):
        best = float('inf') 
        left, right = 1, j - 1
        idx = -1
        while left <= right:
            middle = (left + right) // 2
            if bisect_left(dp[i - 1], dp[i][middle]) <= j - middle:
                idx = middle
                left = middle + 1
            else:
                right = middle - 1
        
        dp[i][j] = 1 + dp[i][idx]

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        if k >= 14:
            return int(1 + log2(n))
        return dp[k][n]

                
        
