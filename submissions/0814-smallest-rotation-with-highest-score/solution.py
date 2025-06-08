class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        diff = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            # width is num
            # offset is num - i
            if num >= len(nums):
                continue
            if num <= i:
                diff[0] += 1
                diff[i - num + 1] -= 1
                diff[i + 1] += 1
                diff[-1] -= 1
            else:
                diff[i + 1] += 1
                diff[len(nums) - num + i + 1] -= 1

        res = []
        curr = 0
        for d in diff:
            curr += d
            res.append(curr)

        m = 0
        ret = 0
        for i, v in enumerate(res):
            if v > m:
                ret = i
                m = v
        
        return ret
        
        
