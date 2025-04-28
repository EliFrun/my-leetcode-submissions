class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        for u in nums1:
            for v in nums2:
                if len(h) < k:
                    heappush(h, (- u - v, [u, v]))
                    continue
                if - u - v > h[0][0]:
                    heappop(h)
                    heappush(h, (- u - v, [u, v]))
                else:
                    break

        return [[u, v] for i, (u, v) in sorted(h)]
        
