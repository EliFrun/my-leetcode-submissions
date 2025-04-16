class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        lis = [0]
        for g in gain:
            lis.append(lis[-1] + g)

        return max(lis)
        
