class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        heapify(nums)
        l = deepcopy(nums)

        ret = 0
        while l and nums:
            if l[0] > nums[0]:
                heappop(nums)
                ret += 1
            heappop(l)

        return ret
        
