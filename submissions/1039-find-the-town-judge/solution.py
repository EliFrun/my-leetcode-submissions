class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n < 2:
            return n
        trusted = defaultdict(set)
        trusts = defaultdict(int)
        for a,b in trust:
            trusts[a] += 1
            trusted[b].add(a)

        keys = trusted.keys()

        #print(trusted)
        #print(trusts)
        for k, v in trusted.items():
            if len(v) < n - 1:
                continue

            if trusts[k] > 0:
                continue

            return k
        return - 1
        
