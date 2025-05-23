class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], n: int) -> int:
        for i in range(len(piles)):
            l = [0]
            for p in piles[i]:
                l.append(l[-1] + p)
            piles[i] = l

        @cache
        def solve(i, k):
            if k <= 0:
                return 0
            if i >= len(piles):
                return 0
            ret = 0
            for j in range(min(k + 1,len(piles[i]))):
                ret = max(ret, piles[i][j] + solve(i + 1, k - j))

            return ret

        return solve(0, n)
