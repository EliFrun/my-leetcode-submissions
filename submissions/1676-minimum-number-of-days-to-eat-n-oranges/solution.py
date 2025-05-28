class Solution:
    def minDays(self, n: int) -> int:
        curr = set([n])
        visited = set()
        layer = -1
        while curr:
            layer += 1
            nxt = set()
            for v in curr:
                visited.add(v)
                if v == 0:
                    return layer
                nxt.add(v - 1)
                if v % 2 == 0:
                    nxt.add(v // 2)
                if v % 3 == 0:
                    nxt.add(v // 3)
            curr = nxt - visited

        return -1
        
