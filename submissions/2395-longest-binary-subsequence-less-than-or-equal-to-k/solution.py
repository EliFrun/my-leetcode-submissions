class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        k = bin(k)[2:]
        if len(s) < len(k):
            return len(s)
        
        @cache
        def solve(i, left):
            if i >= len(s):
                return 0
            if left == 0:
                return 0

            if s[i] == '0' and k[-left] == '1':
                return min(left, len(s) - i)
            
            
            ret = solve(i + 1, left)
            if s[i] == k[- left]:
                ret = max(ret, 1 + solve(i + 1, left - 1))
            return ret
        

        zero_count = 0
        ret = 0
        for i, c in enumerate(s):
            #print(i, zero_count, same_len(i, len(k)), shorter_len(i, len(k) - 1))
            ret = max(
                ret, 
                zero_count + solve(i, len(k))
            )
            if c == '0':
                zero_count += 1
            
        return max(ret, zero_count, len(k) - 1)

        
