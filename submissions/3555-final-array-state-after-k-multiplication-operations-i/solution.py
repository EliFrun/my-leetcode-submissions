class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = []
        for i,v in enumerate(nums):
            heappush(h, (v,i))
        
        for _ in range(k):
            v, i = heappop(h)
            heappush(h, (v * multiplier, i))

        for v, i in h:
            nums[i] = v

        return nums


        
