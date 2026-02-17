class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ret = 0
        for i in range(2 ** len(requests)):
            deltas = [0] * n
            for j, (f,t) in enumerate(requests):
                if (i >> j) & 1:
                    deltas[f] -= 1
                    deltas[t] += 1
            if all(x == 0 for x in deltas):
                ret = max(ret, bin(i).count('1'))
        return ret
        
