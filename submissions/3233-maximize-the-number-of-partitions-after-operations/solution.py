class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def solve(i, incoming=0):
            if i >= len(s):
                return 0 if not incoming else 1
            ch = incoming
            while i < len(s):
                v = 1 << (ord(s[i]) - ord('a'))
                if bin(ch).count('1') == k and not ch & v:
                    break
                
                ch |= v
                i += 1
            return 1 + solve(i)

        if k == 26:
            return solve(0)
        
        ch = [0] * 26
        ret = 0
        cnt = 0
        groups = 0
        for i, c in enumerate(s):
            l = sum([1 for x in ch if x > 0]) 
            if l == k - 1 and cnt >= k and ch[ord(c) - ord('a')] == 0:
                ret = max(ret, groups + 1 + solve(i))
            if l == k:
                if ch[ord(c) - ord('a')] == 0:
                    ch = [0] * 26
                    groups += 1
                    cnt = 0
                else:
                    for j in range(26):
                        cc = chr(ord('a') + j) 
                        if ch[j]:
                            ret = max(ret, groups + 1 + solve(i))
                            continue
                        ret = max(ret, groups + 1 + solve(i + 1, 1 << j))
            cnt += 1
            ch[ord(c) - ord('a')] += 1
        if sum([1 for x in ch if x > 0]):
            groups += 1
        return max(groups, ret)


            
