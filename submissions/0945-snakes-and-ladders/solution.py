class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        l = [-1]
        for i, line in enumerate(board[::-1]):
            if i & 1:
                line = line[::-1]
            l += line

    
        curr = set([1])
        visited = set()
        ret = 0
        while curr:
            nxt = set()
            for n in curr:
                visited.add(n)
                if n == len(l) - 1:
                    return ret
                for i in range(7):
                    foo = n + i
                    if n + i >= len(l):
                        break
                    if i > 0 and l[n + i] != -1:
                        foo = l[n + i]
                    nxt.add(foo)

            curr = nxt - visited
            ret += 1

        return -1
                    
        
