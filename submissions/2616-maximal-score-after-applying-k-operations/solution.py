class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapify(nums)
        ret = 0
        for i in range(k):
            v = heappop(nums)
            ret -= v
            heappush(nums, -ceil(abs(v)/3))

        return ret
        
