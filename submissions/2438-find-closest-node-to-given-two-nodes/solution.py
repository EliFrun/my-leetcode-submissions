class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(n):
            curr = set([n])
            visited = set([-1])
            layer = 0
            ret = [float("inf")] * len(edges)
            while curr:
                nxt = set()
                for node in curr:
                    if node in visited:
                        continue
                    visited.add(node)
                    ret[node] = layer
                    nxt.add(edges[node])

                curr = nxt - visited
                layer += 1
            return ret


        b1 = bfs(node1)
        b2 = bfs(node2)

        best = float('inf')
        ret = -1
        for i, (x,y) in enumerate(list(zip(b1, b2))):
            if max(x,y) < best:
                best = max(x,y)
                ret = i

        return ret

        
