class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        c = defaultdict(int)
        ret = []
        for i, v in enumerate(nums):
            c[v] += 1
            if i >= k:
                c[nums[i - k]] -= 1
            if i >= k - 1:
                l = sorted([(value, key) for key,value in c.items()])
                ret.append(sum([key * value for key, value in l[-x:]]))
        return ret
                    
