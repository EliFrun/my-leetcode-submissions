class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        a = [0] * (len(differences) + 1)
        for i in range(len(differences)):
            a[i + 1] = a[i] + differences[i]

        mi, ma = lower - min(a), upper - max(a)
        
        return max(0, ma - mi + 1)
        
