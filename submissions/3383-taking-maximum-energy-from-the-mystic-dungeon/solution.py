class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ret = float('-inf')
        for i in range(k):
            curr = 0
            for j in reversed(list(range(i, len(energy), k))):
                curr += energy[j]
                ret = max(ret, curr)
        return ret
                

            
