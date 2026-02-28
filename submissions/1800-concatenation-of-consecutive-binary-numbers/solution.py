l = [0] * (10 ** 5 + 1)
curr = 0
shift = 0
nxt = 1
for i in range(int(1e5) + 1):
    if i == nxt:
        nxt *= 2
        shift += 1
    curr = ((curr << shift) + i) % 1_000_000_007
    l[i] = curr

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return l[n]
        
