class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ret = 0
        c = Counter(nums)
        for key in list(c.keys()):
            if k - key in c:
                if key == k - key:
                    diff = c[key] // 2
                    c[key] = 0
                else:
                    diff = min(c[key], c[k - key])
                    c[key] -= diff
                    c[k - key] -= diff
                ret += diff
        return ret
        
