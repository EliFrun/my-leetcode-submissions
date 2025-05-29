class Solution:
    def minJumps(self, arr: List[int]) -> int:
        idx_map = defaultdict(set)
        for i,v in enumerate(arr):
            idx_map[v].add(i)
        
        curr = set([0])
        visited = set()
        layer = 0
        while curr:
            nxt = set()
            seen = set()
            for v in curr:
                if v == len(arr) - 1:
                    return layer
                if v in visited:
                    continue
                visited.add(v)
                if arr[v] == arr[v + 1] and arr[v] == arr[v - 1]:
                    continue
                nxt.add(v + 1)
                if v > 0:
                    nxt.add(v - 1)
                if arr[v] not in seen:
                    nxt |= idx_map[arr[v]]
                    seen.add(v)
            
            curr = nxt - visited
            layer += 1

        return -1
