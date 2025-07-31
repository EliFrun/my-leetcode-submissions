class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = [-x for x in piles]
        heapify(h)
        for _ in range(k):
            heappush(h, -((-heappop(h) + 1)//2))

        return -sum(h)
        
