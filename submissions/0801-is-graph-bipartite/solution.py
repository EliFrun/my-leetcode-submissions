class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = defaultdict(str)
        for i, g in enumerate(graph):
            if i in color:
                continue
            curr_color = 'blue'
            color[i] = 'yellow'
            curr = set(g)
            while curr:
                next_lis = set()
                for i in curr:
                    if i in color:
                        if color[i] != curr_color:
                            return False
                    else:
                        color[i] = curr_color
                        [next_lis.add(x) for x in graph[i]]

                curr_color = 'blue' if curr_color == 'yellow' else 'yellow'
                curr = next_lis
        
        return True
