class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        graphs = []
        must_edges = [(x,y,z) for x,y,z,m in edges if m == 1]
        must_weights = []
        # build graph
        for x,y,z in must_edges:
            must_weights.append(z)
            xi, yi = -1, -1
            for i, graph in enumerate(graphs):
                if x in graph:
                    xi = i
                if y in graph:
                    yi = i

            if xi != -1 and xi == yi:
                return -1
            if xi == -1 and yi == -1:
                graphs.append({x,y})
            elif xi == -1:
                graphs[yi].add(x)
            elif yi == -1:
                graphs[xi].add(y)
            else:
                graphs.append(graphs.pop(max(xi, yi)) | graphs.pop(min(xi, yi)))


        optional_edges = [(-z,x,y) for x,y,z,m in edges if m == 0]
        optional_weights = []
        heapify(optional_edges)
        while optional_edges:
            z,x,y = heappop(optional_edges)
            z *= -1
            xi, yi = -1, -1
            for i, graph in enumerate(graphs):
                if x in graph:
                    xi = i
                if y in graph:
                    yi = i

            if xi != -1 and xi == yi:
                continue
            
            optional_weights.append(z)
            if xi == -1 and yi == -1:
                graphs.append({x,y})
            elif xi == -1:
                graphs[yi].add(x)
            elif yi == -1:
                graphs[xi].add(y)
            else:
                graphs.append(graphs.pop(max(xi, yi)) | graphs.pop(min(xi, yi)))

        
        for i in range(min(k, len(optional_weights))):
            optional_weights[-i - 1] *= 2

        if len(graphs) > 1:
            return -1

        if len(graphs[0]) != n:
            return -1

        return min(min(optional_weights + [float('inf')]), min(must_weights + [float('inf')]))

        
            
        
