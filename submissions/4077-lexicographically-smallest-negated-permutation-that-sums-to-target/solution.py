class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        s = n * (n + 1) // 2
        l = list(range(1, n + 1))
        for i in range(len(l) - 1, -1, -1):
            if s - 2 * l[i] >= target:
                s -= 2 * l[i]
                l[i] *= -1
            
        return sorted(l) if s == target else []
        
