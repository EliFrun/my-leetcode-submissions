class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = [False] * len(nums)
        for v in nums:
            l[v - 1] = True

        c = Counter(nums)
        return (
            [k for k,v in c.items() if v > 1][0],
            [i + 1 for i,v in enumerate(l) if not v][0]
        )

        
