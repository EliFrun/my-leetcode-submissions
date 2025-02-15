class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [x[0] for x in sorted(list(enumerate(mat)), key=lambda x: (sum(x[1]), x[0]))[:k]]
        
