curr = { (1,0, True): 1 }
counts = defaultdict(int)
while curr:
    nxt = defaultdict(int)
    for (v, jump, can_sub), count in curr.items():
        counts[v] += count
        if v > 0 and can_sub:
            nxt[(v - 1, jump, False)] += count
        if v + 2 ** jump <= 1e9:
            nxt[(v + 2 ** jump, jump + 1, True)] += count
    curr = nxt

class Solution:
    def waysToReachStair(self, k: int) -> int:
        return counts[k]

        
