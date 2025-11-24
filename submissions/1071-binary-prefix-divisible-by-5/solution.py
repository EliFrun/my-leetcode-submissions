class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        ret = []
        curr = 0
        for num in nums:
            curr = (num + curr * 2) % 5
            ret.append(curr % 5 == 0)
        return ret
