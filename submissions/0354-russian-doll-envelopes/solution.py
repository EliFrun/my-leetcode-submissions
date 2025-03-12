class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        e.sort(key = lambda x: (x[0], -x[1]))
        e = [x[1] for x in e]

        piles = []
        for num in e:
            i = bisect.bisect_left(piles, num)
            if i == len(piles):
                piles.append(num)
            else:
                piles[i] = num
        return len(piles)

