class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        memo = [0] * (n + k)
        for i in range(n - 1, -1, - 1):
            memo[i] = memo[i + k] +energy[i]
        return max(memo[:n])
                
        
