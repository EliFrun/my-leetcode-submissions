class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return [x for i,x in sorted(sorted(enumerate(nums), key=lambda x: (x[1], x[0]))[-k:])]
