class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stk = [0]
        ret = 0
        for num in nums:
            while stk and stk[-1] >= num:
                if stk[-1] > num:
                    ret += 1
                stk.pop()
            stk.append(num)
        return ret + len(stk) - 1
