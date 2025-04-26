class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tmp = list(reversed(temperatures))
        stk = []
        ret = []
        for i in range(len(tmp)):
            while stk and tmp[i] >= tmp[stk[-1]]:
                stk.pop()
            if stk:
                ret.append(i - stk[-1])
            else:
                ret.append(0)
            stk.append(i)

        return ret[::-1]

        
