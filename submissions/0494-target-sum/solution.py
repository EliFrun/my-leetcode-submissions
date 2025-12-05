class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        curr = { 0: 1 }
        for num in nums:
            nxt = defaultdict(int)
            for k,v in curr.items():
                nxt[k + num] += v
                nxt[k - num] += v
            curr = nxt
        return curr[target] 
