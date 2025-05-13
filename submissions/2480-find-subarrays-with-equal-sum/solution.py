class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for i in range(len(nums) - 1):
            d[nums[i] + nums[i + 1]] += 1

        return any(x >= 2 for x in d.values())

        
