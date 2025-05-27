class Solution:
    def getFinalState(self, nums: List[int], k: int, m: int) -> List[int]:
        M = 1_000_000_007
        if m == 1:
            return nums
        if len(nums) == 1:
            return [(nums[0] * pow(m, k, M)) % M]
        
        s = SortedList()
        for i, num in enumerate(nums):
            s.add([num, i, 0])

        while k > 0 and s[-1][0] / s[0][0] >= m:
            v = s.pop(0)
            v[0] *= m
            s.add(v)
            k -= 1

        
        s = list(s)
        for i in range(len(s)):
            s[i][2] += k // len(s) + (1 if i < k % len(s) else 0)

        for num, i, e in s:
            nums[i] = (num * pow(m, e, M)) % M

        return nums

        
