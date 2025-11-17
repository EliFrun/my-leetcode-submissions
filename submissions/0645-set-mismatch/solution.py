class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ret = [-1,-1]
        c = Counter(nums)
        for i in range(1, len(nums) + 1):
            if i not in c:
                ret[1] = i
            if c[i] == 2:
                ret[0] = i
        return ret
        
