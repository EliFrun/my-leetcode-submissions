class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ret = []
        curr = []
        for num in nums:
            if not curr:
                curr.append(num)
            elif num <= curr[0] + k:
                curr.append(num)
            else:
                return []
            if len(curr) == 3:
                ret.append(curr)
                curr = []

        return ret
