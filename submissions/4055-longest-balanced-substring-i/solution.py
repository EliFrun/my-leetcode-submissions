class Solution:
    def longestBalanced(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            cnt = defaultdict(int)
            for j in range(i, len(s)):
                cnt[s[j]] += 1
                if all(cnt[k] == cnt[s[i]] for k in cnt.keys()):
                    ret = max(ret, j - i + 1)

        return ret

        
