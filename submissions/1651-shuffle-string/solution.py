class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([x[1] for x in sorted(list(zip(indices, s)))])
        
