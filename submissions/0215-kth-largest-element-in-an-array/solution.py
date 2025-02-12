class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            if len(q) < k:
                heapq.heappush(q, num)
            elif len(q) == k:
                heapq.heappush(q, max(heapq.heappop(q), num))


        return heapq.heappop(q)
        
