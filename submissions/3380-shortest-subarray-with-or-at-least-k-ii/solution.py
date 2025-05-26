class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def solve(left, right):
            num = [r - l for l,r in zip(prefix[left], prefix[right])]
            ret = 0
            for i in range(len(num)):
                ret += (1 if num[i] > 0 else 0) * (2 ** i)

            return ret

        
        prefix = [tuple([0] * max(int(log2(1 + x) + 1) for x in nums))]
        for num in nums:
            curr = list(prefix[-1])
            idx = 0
            while num > 0:
                curr[idx] += num & 1
                num >>= 1
                idx += 1
            prefix.append(tuple(curr))


        if solve(0, len(prefix) - 1) < k:
            return -1

        res = float('inf')
        for i in range(1, len(prefix)):
            if solve(0, i) < k:
                continue
            left, right = 0, i - 1
            ret = -1
            while left <= right:
                if i - right > res:
                    break
                middle = (left + right) // 2
                if solve(middle, i) >= k:
                    ret = middle
                    left = middle + 1
                else:
                    right = middle - 1
            if ret >= 0:
                res = min(res, i - ret)

        return res

            
            
        
