class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        M = 1_000_000_007
        l = []
        word += ' '
        curr = ''
        cnt = 0
        for c in word:
            if c == curr:
                cnt += 1
            else:
                l.append(cnt)
                curr = c
                cnt = 1
        l.pop(0)

        ret = 1
        for v in l:
            ret = (ret * v) % M

        if len(l) >= k:
            return ret
        
        dp = [0] * (k)
        dp[len(l)] = 1
        for i in range(len(l)):
            l[i] -= 1
            prefix = [0]
            for v in dp:
                prefix.append(prefix[-1] + v)
            for j in range(len(dp) - 1, len(l) - 1, -1):
                dp[j] = (dp[j] + prefix[j] - prefix[max(0, j - l[i])]) % M


        return (M + ret - sum(dp)) % M
            
        
