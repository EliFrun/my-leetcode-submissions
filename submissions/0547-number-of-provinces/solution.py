class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        ret = 0
        for i in range(len(isConnected)):
            if i in visited:
                continue
            ret += 1
            curr = set([i])
            while curr:
                nxt = set()
                for j in curr:
                    if j in visited:
                        continue
                    visited.add(j)
                    nxt.update([i for i,v in enumerate(isConnected[j]) if v])

                curr = nxt - visited

        return ret
                        
        
