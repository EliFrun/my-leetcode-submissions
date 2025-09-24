class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def is_valid(g1, g2):
            ret = 0
            for x,y in zip(g1,g2):
                if x != y:
                    ret += 1
                    if ret > 1:
                        return False
            return True
        
        curr = set([startGene])
        cnt = -1
        visited = set()
        while curr:
            cnt += 1
            nxt = set()
            for gene in curr:
                if gene in visited:
                    continue
                visited.add(gene)
                if gene == endGene:
                    return cnt
                for g in bank:
                    if is_valid(gene, g):
                        nxt.add(g)
            curr = nxt - visited
        return -1
        
