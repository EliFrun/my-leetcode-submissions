class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ret = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()
            idx = stk[-1] if stk else i
            ret.append(idx - i)
            stk.append(i)
        return ret[::-1]
        
