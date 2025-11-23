class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        M = 1_000_000_007
        prefix = [0]
        for c in s:
            prefix.append(prefix[-1] + int(c))
        if prefix[-1] == 0:
            return [0] * len(queries)
        
        queries.sort()
        non_zero_count = 0
        v = 0
        counts = [0]
        mods = [0]
        for c in s:
            if c != '0':
                non_zero_count += 1
                v = (10 * v + int(c)) % M
            mods.append(v)
            counts.append(non_zero_count)

        ret = []
        for l, r in queries:
            cnt = prefix[r + 1] - prefix[l]
            st = (M + mods[r + 1] - mods[l] * pow(10, counts[r + 1] - counts[l], M)) % M
            ret.append((cnt * st) % M)
        return ret
            
        
