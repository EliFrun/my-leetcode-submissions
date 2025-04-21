class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        ret = curr / k
        for i in range(k, len(nums)):
            curr -= nums[i - k]
            curr += nums[i]
            ret = max(ret, curr / k)

        return ret
