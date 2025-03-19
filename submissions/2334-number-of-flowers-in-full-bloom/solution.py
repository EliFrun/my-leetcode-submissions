class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        a = SortedList([x[0] for x in flowers])
        b = SortedList([x[1] for x in flowers])

        return [a.bisect_right(p) - b.bisect_left(p) for p in people]



