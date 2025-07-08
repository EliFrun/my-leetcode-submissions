class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        h = []
        for _, v in c.items():
            heappush(h, v)


        for _ in range(k):
            if not h:
                break
            v = heappop(h)
            v -= 1
            if v > 0:
                heappush(h, v)

        return len(h)
