class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = [0]
        ret = []
        for p in prices[::-1]:
            while p < stk[-1]:
                stk.pop()
            ret.append(p - stk[-1])
            stk.append(p)
        return ret[::-1]

