class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        a = SortedList([])
        ret = 0
        for n in instructions:
            ret += min(a.bisect_left(n), len(a) - a.bisect_right(n))
            a.add(n)

        return ret % 1_000_000_007
        
