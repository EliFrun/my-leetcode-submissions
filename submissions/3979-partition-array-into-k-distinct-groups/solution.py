class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        groups_needed = len(nums) / k
        if int(groups_needed) != groups_needed:
            return False

        c = Counter(nums)
        if max(c.values()) > groups_needed:
            return False

        return True
        
