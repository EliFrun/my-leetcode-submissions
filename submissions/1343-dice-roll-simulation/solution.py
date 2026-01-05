class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        m = max(rollMax)
        curr = [[0] * m for _ in range(6)]
        for i in range(6):
            curr[i][0] = 1


        for _ in range(n - 1):
            nxt = [[0] + curr[i][:rollMax[i] - 1] for i in range(6)]
            s = [0] * 6
            for i in range(6):
                s[i] = sum(curr[i])
            ss = sum(s)
            for i in range(6):
                nxt[i][0] = ss - s[i]
            curr = nxt

        return sum(sum(x) for x in curr) % 1_000_000_007
            
