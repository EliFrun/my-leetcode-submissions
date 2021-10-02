class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(sorted(''.join([str(x) for x in nums]).split('0'), key=len)[-1])
