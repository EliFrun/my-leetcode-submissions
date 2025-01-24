class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ret = []
        inedges = [set() for _ in range(len(graph))]
        for i, v in enumerate(graph):
            for n in v:
                inedges[n].add(i)
        print(inedges)

        graph = [(i,set(v)) for i,v in enumerate(graph)]

        prev = set()
        curr = set([i for i,v in graph])
        while prev != curr:
            nxt = curr.copy()
            for i in curr:
                if len(graph[i][1]) == 0:
                    for j in inedges[i]:
                        graph[j][1].remove(i)
                    nxt.remove(i)

            prev = curr 
            curr = nxt

        return [i for i,v in graph if len(v) == 0]
            


        
            
