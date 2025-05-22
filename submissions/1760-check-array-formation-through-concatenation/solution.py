class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        lis = []
        idxs = {}
        for i, piece in enumerate(pieces):
            for v in piece:
                idxs[v] = i

        for v in arr:
            if v in lis:
                continue
            if v not in idxs:
                return False
            lis.extend(pieces[idxs[v]])

        return len(lis) == len(arr) and all(x == y for x,y in zip(arr, lis))
        
