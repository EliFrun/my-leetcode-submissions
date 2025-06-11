class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        for v in [-1, 1]:
            ret = 0
            prev = -1
            for i, val in enumerate(nums):
                if val == v:
                    if prev == -1:
                        prev = i
                    else:
                        ret += i - prev
                        prev = -1

            if ret <= k and prev == -1:
                return True
        return False
                    
