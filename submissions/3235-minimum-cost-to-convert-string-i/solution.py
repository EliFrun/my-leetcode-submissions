class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g = defaultdict(list)
        for o,c,v in zip(original, changed, cost):
            g[ord(o) - ord('a')].append((ord(c) - ord('a') ,v))

        mp = []
        for i in range(26):
            dp = [float('inf')] * 26
            q = [(0, i)]
            while q:
                cost, c = heappop(q)
                if dp[c] <= cost:
                    continue
                dp[c] = cost
                for nxt, v in g[c]:
                    heappush(q, (cost + v, nxt))

            mp.append(dp)
        ret = 0
        for s,t in zip(source, target):
            s = ord(s) - ord('a')
            t = ord(t) - ord('a')
            d = mp[s][t]
            if d == float('inf'):
                return -1
            ret += d
        return ret

        
