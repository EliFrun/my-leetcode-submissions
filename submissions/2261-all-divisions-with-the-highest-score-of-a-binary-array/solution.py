class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        idxs = [0]
        score = sum(nums)
        best = score
        for i,num in enumerate(nums):
            score += 1 - 2 * num
            if score > best:
                best = score
                idxs = [i + 1]
            elif score == best:
                idxs.append(i + 1)

        return idxs
        
