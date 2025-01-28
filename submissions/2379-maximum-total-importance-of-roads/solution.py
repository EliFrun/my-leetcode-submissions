class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        nodes = defaultdict(set)
        for i,j in roads:
            nodes[i].add(j)
            nodes[j].add(i)

        return sum([x * n for x, n in zip(sorted([len(a) for a in nodes.values()], reverse=True), list(range(n, 0, -1)))])
        
