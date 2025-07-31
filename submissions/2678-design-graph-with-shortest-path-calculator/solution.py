class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[0] * n for _ in range(n)]
        for p,c,w in edges:
            self.graph[p][c] = w
        

    def addEdge(self, edge: List[int]) -> None:
        p,c,w = edge
        self.graph[p][c] = w
        

    def shortestPath(self, node1: int, node2: int) -> int:
        h = [(0, node1)]
        visited = set()
        while h and h[0][1] != node2:
            distance, node = heappop(h)
            if node in visited:
                continue
            visited.add(node)
            for i, w in enumerate(self.graph[node]):
                if w == 0:
                    continue
                heappush(h, (distance + w, i))

        return h[0][0] if h else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
