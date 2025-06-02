class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        d = {}
        a = defaultdict(int)
        for idx, (r1,c1,r2,c2) in enumerate(artifacts):
            for dr in range(r1, r2 + 1):
                for dc in range(c1, c2 + 1):
                    a[idx] += 1
                    d[(dr, dc)] = idx

        for dr, dc in dig:
            if (dr, dc) in d:
                a[d[(dr, dc)]] -= 1

        return len([k for k, v in a.items() if v == 0])

        
