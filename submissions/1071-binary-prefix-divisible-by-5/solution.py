class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ret = []
        curr = 0
        for num in nums:
            curr = (curr * 2 + num) % 5
            ret.append(curr == 0)

        return ret
        
