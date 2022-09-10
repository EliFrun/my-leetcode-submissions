class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        total = sum(nums)
        diff = abs(total - goal)
        return diff // limit + (1 if diff % limit != 0 else 0)
        
