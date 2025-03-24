class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ret = 0
        meetings.sort()
        curr = 0
        for start, end in meetings:
            if start > curr:
                ret += start - curr - 1
            curr = max(curr, end)

        ret += days - min(days, curr)
        return ret


            
