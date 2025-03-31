class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        lis = []
        for i in range(len(weights) - 1):
            lis.append(weights[i] + weights[i + 1])
        lis.sort()
        return sum(lis[len(lis) - k + 1:]) - sum(lis[:k - 1])

