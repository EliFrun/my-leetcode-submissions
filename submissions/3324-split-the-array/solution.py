class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return all(x < 3 for x in Counter(nums).values())
        
