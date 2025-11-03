class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ret = 0
        curr = ''
        s = 0
        m = 0
        for i, c in enumerate(colors):
            if c == curr:
                s += neededTime[i]
                m = max(m, neededTime[i])
            else:
                curr = c
                ret += s - m
                s = neededTime[i]
                m = neededTime[i]

        ret += s - m
        return ret
