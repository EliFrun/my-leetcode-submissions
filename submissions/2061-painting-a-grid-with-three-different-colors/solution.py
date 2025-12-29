class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        l = set(['0', '1', '2'])
        for _ in range(m - 1):
            nxt = set()
            for seq in l:
                for i in range(3):
                    if str(i) != seq[-1]:
                        nxt.add(seq + str(i))
            l = nxt
        
        l = sorted(list(l))
        transition_function = defaultdict(set)
        for i, seq in enumerate(l):
            for j, seq2 in enumerate(l):
                if all(s1 != s2 for s1,s2 in zip(seq, seq2)):
                    transition_function[i].add(j)

        dp = [[0] * len(l) for _ in range(n)]
        dp[0] = [1] * len(l)
        for i in range(1, n):
            for j in range(len(dp[0])):
                for k in transition_function[j]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % 1_000_000_007

        return sum(dp[-1]) % 1_000_000_007


       
            
        
