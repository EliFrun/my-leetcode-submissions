class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ret = set()
        i = 0
        while i < len(nums):
            if nums[i] == key:
                j = max(0, i - k)
                limit = min(i + k + 1, len(nums))
                while j < limit:
                    ret.add(j)
                    if nums[j] == key:
                        limit = min(j + k + 1, len(nums))
                    j += 1
                i = j - 1
            i += 1
            
        return sorted(list(ret))
